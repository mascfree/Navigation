import pandas as pd
from Utils.Helper import measure_performance
class IP:
    """
    Implementa el algoritmo de Iteración de Políticas para resolver problemas de decisión en un grafo.

    Atributos:
        graph (Graph): El grafo que contiene los estados y transiciones.
        gamma (float): El factor de descuento para la iteración de políticas.
        threshold (float): El umbral de convergencia para la evaluación de políticas.
        actions (list): Una lista de acciones posibles.
        standard_cost (int): El costo estándar para las transiciones entre estados.
        deadend_cost (int): El costo asociado a los estados sin salida (deadend).
    """    
    def __init__(self, graph, gamma=0.8, threshold=0.01, standard_cost=1, deadend_cost=1):
        self.graph = graph
        self.gamma = gamma
        self.threshold = threshold
        self.actions = ["N", "S", "E", "W"]
        self.standard_cost = standard_cost
        self.deadend_cost = deadend_cost

    def policy_evaluation(self, policy, values):
        """
        Evalúa una política dada actualizando los valores de los estados hasta la convergencia.

        Args:
            policy (dict): La política a evaluar.
            values (dict): Los valores actuales de los estados.

        Returns:
            int: El número de iteraciones realizadas para la evaluación de la política.
        """        
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
        """
        Mejora la política actual basándose en los valores de los estados.

        Args:
            policy (dict): La política actual a mejorar.
            values (dict): Los valores actuales de los estados.

        Returns:
            bool: True si la política se mantiene estable, False si ha sido modificada.
        """        
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
        """
        Realiza el algoritmo de Iteración de Políticas para encontrar la política óptima y los valores de los estados.

        Returns:
            tuple: Una tupla que contiene la política óptima, los valores de los estados y el número de iteraciones realizadas.
        """        
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
        """
        Imprime los resultados de la iteración de políticas, incluyendo la política óptima y los valores de los estados.
        """        
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

    def state_to_coordinates(self, state):
        """
        Convierte un estado en coordenadas (x, y) en la matriz.
        
        :param state: El estado a convertir, que puede ser una cadena que representa un número.
        :return: Una tupla (x, y) representando las coordenadas en la matriz.
        """
        # Asegurarse de que el estado es un entero
        state = int(state) - 1  # Restar 1 para que los estados comiencen desde 0

        # Tamaño de la matriz
        num_rows, num_cols =  self.graph.matrix_size

        # Calcular las coordenadas basadas en el estado
        x = state // num_cols
        y = state % num_cols

        # Verificar que las coordenadas están dentro de los límites de la matriz
        if x >= num_rows or y >= num_cols:
            raise ValueError(f"Coordenadas fuera de los límites: ({x}, {y}) para el estado {state + 1}")

        return (x, y)

    @measure_performance
    def print1(self):
        """
        Imprime los resultados de la iteración de políticas en una matriz, 
        incluyendo la dirección y la flecha de su sentido.
        """
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
        
        # Tamaño de la matriz
        matrix_size =  self.graph.matrix_size
        matrix = [['' for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
        
        for state, row in result_df.iterrows():
            x, y = self.state_to_coordinates(state)  # Función que convierte el estado en coordenadas de la matriz
            matrix[x][y] = f"{state} {row['Policy']}"
        
        # Imprimir gamma y threshold
        print(f"Gamma: {self.gamma}")
        print(f"Threshold: {self.threshold}")
        # Imprimir la matriz
        print("Policy Iteration Results Matrix:")
        for row in matrix:
            print("    ".join(row).strip())
        print(f"Numero de Iteraciones: {iterations}")

        
