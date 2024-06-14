class Action:
    """
    Representa una acción en un grafo, con una dirección y una probabilidad asociada.

    Atributos:
        direction (str): La dirección de la acción.
        probability (float): La probabilidad de que ocurra la acción.
    """    
    def __init__(self, direction, probability):
        self.direction = direction
        self.probability = probability

    def __str__(self):
        return f"Direccion: {self.direction}, direccion: {self.probability}"
