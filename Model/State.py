class State:
    """
    Representa un estado en un grafo, con atributos adicionales para indicar si es un objetivo o un callejón sin salida, así como un valor heurístico.

    Atributos:
        name (str): El nombre del estado.
        is_goal (bool): Indica si el estado es un objetivo final.
        is_deadend (bool): Indica si el estado es un callejón sin salida.
        heuristic (int): El valor heurístico asociado al estado.
        edges (list): Una lista de aristas (Edge) que parten de este estado.
    """    
    def __init__(self, name, is_goal=False, is_deadend=False, heuristic=0):
        self.name = name
        self.is_goal = is_goal
        self.is_deadend = is_deadend
        self.heuristic = heuristic
        self.edges = []

    def __str__(self):
        return self.name
