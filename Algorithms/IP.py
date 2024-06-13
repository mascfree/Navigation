import pandas as pd
from Utils.Helper import measure_performance
class IP:
    def __init__(self, graph, gamma=0.8, threshold=0.01, standard_cost=1, deadend_cost=1):
        self.graph = graph
        self.gamma = gamma
        self.threshold = threshold
        self.actions = ["N", "S", "E", "W"]
        self.standard_cost = standard_cost
        self.deadend_cost = deadend_cost

    def policy_evaluation(self, policy, values):
        iterations = 0
        while True:
            delta = 0
            for node in self.graph.nodes.values():
                v = values[node.state.name]
                new_value = 0
                for edge in node.state.edges:
                    next_state = edge.target.name
                    action_prob = policy[node.state.name][edge.action.direction]
                    prob = edge.action.probability
                    if edge.target.is_goal:
                        cost = 0
                    elif edge.target.is_deadend:
                        cost = self.deadend_cost
                    else:
                        cost = self.standard_cost
                    new_value += action_prob * prob * (cost + self.gamma * values[next_state])
                values[node.state.name] = new_value
                delta = max(delta, abs(v - new_value))
            iterations +=1
            if delta < self.threshold:
                break
        return iterations

    def policy_improvement(self, policy, values):
        policy_stable = True
        for node in self.graph.nodes.values():
            old_action = max(policy[node.state.name], key=policy[node.state.name].get)
            action_values = {action: 0 for action in self.actions}
            for edge in node.state.edges:
                next_state = edge.target.name
                prob = edge.action.probability
                if edge.target.is_goal:
                    cost = 0
                elif edge.target.is_deadend:
                    cost = self.deadend_cost
                else:
                    cost = self.standard_cost
                action_values[edge.action.direction] += prob * (cost + self.gamma * values[next_state])
            best_action = min(action_values, key=action_values.get)
            policy[node.state.name] = {a: 1 if a == best_action else 0 for a in self.actions}
            if old_action != best_action:
                policy_stable = False
        return policy_stable

    def policy_iteration(self):
        values = {node.state.name: 0 for node in self.graph.nodes.values()}
        policy = {node.state.name: {action: 1/len(self.actions) for action in self.actions} for node in self.graph.nodes.values()}
        iterations = 0
        while True:
            iter_eval  = self.policy_evaluation(policy, values)
            iterations += iter_eval 
            if self.policy_improvement(policy, values):
                break
        return policy, values, iterations
    
    @measure_performance
    def print(self):
        optimal_policy, optimal_values, iterations = self.policy_iteration()
    
        # Crear un DataFrame para mostrar la política y el estado de destino
        policy_df = pd.DataFrame(optimal_policy).T
        policy_df.columns = ['North', 'South', 'East', 'West']
        policy_df.index.name = 'State'

        # Crear un DataFrame para mostrar los valores
        values_df = pd.DataFrame(optimal_values.items(), columns=['State', 'Value'])

        # Unir ambos DataFrames
        result_df = policy_df.join(values_df.set_index('State'))

        # Agregar una columna de flechas basada en la política óptima
        arrow_map = {'North': '↑', 'South': '↓', 'East': '→', 'West': '←'}
        def get_arrow(row):
            best_action = max((row[action], action) for action in ['North', 'South', 'East', 'West'] if pd.notnull(row[action]))
            return arrow_map[best_action[1]]
        result_df['Policy'] = result_df.apply(get_arrow, axis=1)

        # Filtrar para excluir nodos deadend
        deadend_states = [node.state.name for node in self.graph.nodes.values() if node.state.is_deadend]
        result_df = result_df[~result_df.index.isin(deadend_states)]    
            
        # Mostrar los DataFrames
        print("Policy Iteration Results:")
        print(result_df)
        print(f"Numero de Iteraciones:{iterations}")