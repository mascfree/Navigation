class Node:
    """
    Representa un nodo en un grafo, encapsulando un estado.

    Atributos:
        state (State): El estado asociado a este nodo.
    """    
    def __init__(self, state):
        self.state = state

    def __str__(self):
        return str(self.state)
