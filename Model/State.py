class State:
    def __init__(self, name, is_goal=False, is_deadend=False, heuristic=0):
        """
        Inicializa un estado con un nombre y opciones adicionales.

        Args:
            nombre (str): Nombre del estado.
            es_meta (bool, opcional): Indica si el estado es una meta (por defecto False) key goal.
            es_mortal (bool, opcional): Indica si el estado es mortal (por defecto False) key deadend.
            heuristica (float, opcional): Valor de la heurística asociada al estado (por defecto 0).
        """
        self.name = name
        self.is_goal = is_goal
        self.is_deadend = is_deadend
        self.heuristic = heuristic
        self.edges = []

    def __str__(self):
        return self.name
