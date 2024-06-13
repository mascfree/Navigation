class Edge:
    def __init__(self, source, target, action):
        self.source = source
        self.target = target
        self.action = action

    def __str__(self):
        return f"Origen: {self.source}, Destino: {self.target}, Accion: {self.action}"
