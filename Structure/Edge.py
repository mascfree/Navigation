class Edge:
    """
    Representa una arista en un grafo con un nodo origen, un nodo destino y una acción asociada.

    Atributos:
        source (str): El nodo de origen de la arista.
        target (str): El nodo de destino de la arista.
        action (str): La acción asociada a la arista.
    """    
    def __init__(self, source, target, action):
        self.source = source
        self.target = target
        self.action = action

    def __str__(self):
        return f"Origen: {self.source}, Destino: {self.target}, Accion: {self.action}"
