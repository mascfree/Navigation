from Estructura.Arista import Arista
from Estructura.Nodo import Nodo

class Grafo:
    def __init__(self):
        """
        Inicializa un grafo vacío.
        """
        self.nodos = {}

    def agregar_nodo(self, estado):
        """
        Agrega un nuevo nodo al grafo.

        Args:
            estado: Objeto que representa el estado del nodo a agregar.
        """
        nodo = Nodo(estado)
        self.nodos[estado.nombre] = nodo

    def agregar_arista(self, origen, destino, accion):
        """
        Agrega una nueva arista al grafo entre los nodos especificados.

        Si alguno de los nodos no existe en el grafo, los agrega primero.

        Args:
            origen: Objeto que representa el nodo de origen de la arista.
            destino: Objeto que representa el nodo de destino de la arista.
            accion: Descripción de la acción asociada a la arista.
        """
        if origen.nombre not in self.nodos:
            self.agregar_nodo(origen)
        if destino.nombre not in self.nodos:
            self.agregar_nodo(destino)
        arista = Arista(origen, destino, accion)
        self.nodos[origen.nombre].estado.aristas.append(arista)

    def imprimir_nodos(self):
        """
        Imprime los nombres de todos los nodos en el grafo.
        """
        print("Nodos:")
        for nombre in self.nodos:
            print(nombre)

    def imprimir_aristas(self):
        """
        Imprime las aristas en el grafo, mostrando los nodos de origen y destino,
        así como la acción asociada a cada arista.
        """
        print("Aristas:")
        for nombre, nodo in self.nodos.items():
            for arista in nodo.estado.aristas:
                print(f"Origen: {nombre}, Destino: {arista.destino.nombre}, Accion: {arista.accion}")

    def imprimir_aristas_de_nodo(self, nombre_nodo):
        """
        Imprime las aristas del nodo especificado, mostrando los nodos de destino
        y la acción asociada a cada arista.

        Args:
            nombre_nodo: Nombre del nodo del cual se desean imprimir las aristas.
        """
        if nombre_nodo in self.nodos:
            print(f"Aristas del nodo {nombre_nodo}:")
            for arista in self.nodos[nombre_nodo].estado.aristas:
                print(f"Destino: {arista.destino.nombre}, Accion: {arista.accion}")
        else:
            print(f"No se encontró el nodo {nombre_nodo}")
