class Arista:
    def __init__(self, origen, destino, accion):
        """
        Inicializa una arista con un nodo de origen, un nodo de destino y una acción.

        Args:
            origen (Nodo): Nodo de origen de la arista.
            destino (Nodo): Nodo de destino de la arista.
            accion (Accion): Acción asociada a la arista.
        """
        self.origen = origen
        self.destino = destino
        self.accion = accion

    def __str__(self):
        """
        Devuelve una representación en cadena de la arista.

        Returns:
            str: Cadena que representa la arista y sus componentes.
        """
        return f"Origen: {self.origen}, Destino: {self.destino}, Accion: {self.accion}"
