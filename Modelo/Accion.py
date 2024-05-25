class Accion:
    def __init__(self, direccion, probabilidad):
        """
        Inicializa una acción con una dirección y una probabilidad asociadas.

        Args:
            direccion (str): Dirección de la acción.
            probabilidad (float): Probabilidad de que la acción tenga éxito.
        """
        self.direccion = direccion
        self.probabilidad = probabilidad

    def __str__(self):
        """
        Devuelve una representación en cadena de la acción.

        Returns:
            str: Cadena que representa la acción y su probabilidad.
        """
        return f"Accion: {self.direccion}, Probabilidad: {self.probabilidad}"
