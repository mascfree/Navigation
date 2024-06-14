import pandas as pd
from Utils.Helper import measure_performance

class IV:
    """
    Implementa el algoritmo de Iteración de Valores para resolver problemas de decisión en un grafo.

    Atributos:
        graph (Graph): El grafo que contiene los estados y transiciones.
        gamma (float): El factor de descuento para la iteración de valores.
        threshold (float): El umbral de convergencia para la iteración de valores.
        standard_cost (int): El costo estándar para las transiciones entre estados.
        deadend_cost (int): El costo asociado a los estados sin salida (deadend).
        values (dict): Un diccionario que almacena los valores de los estados.
        actions (list): Una lista de acciones posibles.
    """

    def __init__(self, graph, gamma=0.8, threshold=0.01, standard_cost=1, deadend_cost=1):
        self.graph = graph
        self.gamma = gamma
        self.threshold = threshold
        self.standard_cost = standard_cost
        self.deadend_cost = deadend_cost
        self.values = {node.state.name: 0 for node in graph.nodes.values()}
        self.actions = ["N", "S", "E", "W"]

    def value_iteration(self):
        """
        Realiza el algoritmo de Iteración de Valores para encontrar la política óptima y los valores de los estados.

        Returns:
            tuple: Una tupla que contiene la política óptima, los valores de los estados y el número de iteraciones realizadas.
        """        
        iterations = 0
        while True:
            delta = 0
            for node in self.graph.nodes.values():
                state = node.state
                v = self.values[state.name]
                action_values = {action: 0 for action in self.actions}
                for edge in state.edges:
                    next_state = edge.target.name
                    action = edge.action
                    if self.graph.nodes[next_state].state.is_goal:
                        cost = 0  # Costo cero para el estado objetivo
                    elif self.graph.nodes[next_state].state.is_deadend:
                        cost = self.deadend_cost
                    else:
                        cost = self.standard_cost
                    action_values[action.direction] += action.probability * (cost + self.gamma * self.values[next_state])
                self.values[state.name] = min(action_values.values())
                delta = max(delta, abs(v - self.values[state.name]))
            iterations +=1
            if delta < self.threshold:
                break
        # Derivar la política óptima a partir de los valores
        policy = {}
        for node in self.graph.nodes.values():
            state = node.state
            action_values = {action: 0 for action in self.actions}
            for edge in state.edges:
                next_state = edge.target.name
                action = edge.action
                if self.graph.nodes[next_state].state.is_goal:
                    cost = 0  # Costo cero para el estado objetivo
                elif self.graph.nodes[next_state].state.is_deadend:
                    cost = self.deadend_cost
                else:
                    cost = self.standard_cost
                action_values[action.direction] += action.probability * (cost + self.gamma * self.values[next_state])
            best_action = min(action_values, key=action_values.get)
            policy[state.name] = {a: 1 if a == best_action else 0 for a in self.actions}
        return policy, self.values, iterations

    @measure_performance
    def print(self):
        """
        Imprime los resultados de la iteración de valores, incluyendo la política óptima y los valores de los estados.
        """        
        value_policy, value_values, iterations = self.value_iteration()

        # Crear un DataFrame para mostrar la política y el estado de destino
        value_policy_df = pd.DataFrame(value_policy).T
        value_policy_df.columns = ['North', 'South', 'East', 'West']
        value_policy_df.index.name = 'State'

        # Crear un DataFrame para mostrar los valores
        value_values_df = pd.DataFrame(value_values.items(), columns=['State', 'Value'])

        # Unir ambos DataFrames
        value_result_df = value_policy_df.join(value_values_df.set_index('State'))

        # Agregar una columna de flechas basada en la política óptima
        arrow_map = {'North': '↑', 'South': '↓', 'East': '→', 'West': '←'}
        def get_arrow(row):
            best_action = max((row[action], action) for action in ['North', 'South', 'East', 'West'] if pd.notnull(row[action]))
            return arrow_map[best_action[1]]
        value_result_df['Policy'] = value_result_df.apply(get_arrow, axis=1)       

        # Filtrar para excluir nodos deadend
        deadend_states = [node.state.name for node in self.graph.nodes.values() if node.state.is_deadend]
        value_result_df = value_result_df[~value_result_df.index.isin(deadend_states)]

        # Mostrar los DataFrames
        print("\nValue Iteration Results:")
        print(value_result_df)
        print(f"Numero de Iteraciones: {iterations}")
            
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
        Imprime los resultados de la iteración de valores en una matriz,
        incluyendo la dirección y la flecha de su sentido.
        """
        value_policy, value_values, iterations = self.value_iteration()

        # Crear un DataFrame para mostrar la política y el estado de destino
        value_policy_df = pd.DataFrame(value_policy).T
        value_policy_df.columns = ['North', 'South', 'East', 'West']
        value_policy_df.index.name = 'State'

        # Crear un DataFrame para mostrar los valores
        value_values_df = pd.DataFrame(value_values.items(), columns=['State', 'Value'])

        # Unir ambos DataFrames
        value_result_df = value_policy_df.join(value_values_df.set_index('State'))

        # Agregar una columna de flechas basada en la política óptima
        arrow_map = {'North': '↑', 'South': '↓', 'East': '→', 'West': '←'}
        
        def get_arrow(row):
            best_action = max((row[action], action) for action in ['North', 'South', 'East', 'West'] if pd.notnull(row[action]))
            return arrow_map[best_action[1]]
        
        value_result_df['Policy'] = value_result_df.apply(get_arrow, axis=1)

        # Filtrar para excluir nodos deadend
        deadend_states = [node.state.name for node in self.graph.nodes.values() if node.state.is_deadend]
        value_result_df = value_result_df[~value_result_df.index.isin(deadend_states)]

        # Tamaño de la matriz
        matrix_size =  self.graph.matrix_size
        matrix = [['' for _ in range(matrix_size[1])] for _ in range(matrix_size[0])]
        
        for state, row in value_result_df.iterrows():
            x, y = self.state_to_coordinates(state)  # Función que convierte el estado en coordenadas de la matriz
            matrix[x][y] = f"{state} {row['Policy']}"
        
        # Imprimir gamma y threshold
        print(f"Gamma: {self.gamma}")
        print(f"Threshold: {self.threshold}")
        # Imprimir la matriz
        print("Value Iteration Results Matrix:")
        for row in matrix:
            print("    ".join(row).strip())
        print(f"Numero de Iteraciones: {iterations}")            