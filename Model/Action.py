class Action:
    def __init__(self, direction, probability):
        """
        Inicializa una acción con una dirección y una probabilidad asociadas.

        Args:
            direccion (str): Dirección de la acción.
            probabilidad (float): Probabilidad de que la acción tenga éxito.
        """
        self.direction = direction
        self.probability = probability

    def __str__(self):
        """
        Devuelve una representación en cadena de la acción.

        Returns:
            str: Cadena que representa la acción y su probabilidad.
        """
        return f"Direccion: {self.direction}, direccion: {self.probability}"
