class Nodo:
    def __init__(self, estado):
        """
        Inicializa un nodo con un estado dado.

        Args:
            estado (Estado): Estado asociado al nodo.
        """
        self.estado = estado

    def __str__(self):
        """
        Devuelve una representación en cadena del nodo.

        Returns:
            str: Cadena que representa el estado del nodo.
        """
        return str(self.estado)
