class Estado:
    def __init__(self, nombre, es_meta=False, es_mortal=False, heuristica=0):
        """
        Inicializa un estado con un nombre y opciones adicionales.

        Args:
            nombre (str): Nombre del estado.
            es_meta (bool, opcional): Indica si el estado es una meta (por defecto False) key goal.
            es_mortal (bool, opcional): Indica si el estado es mortal (por defecto False) key deadend.
            heuristica (float, opcional): Valor de la heurística asociada al estado (por defecto 0).
        """
        self.nombre = nombre
        self.es_meta = es_meta
        self.es_mortal = es_mortal
        self.heuristica = heuristica
        self.aristas = []  # Lista de aristas conectadas a este estado

    def __str__(self):
        """
        Devuelve el nombre del estado.

        Returns:
            str: Nombre del estado.
        """
        return self.nombre
