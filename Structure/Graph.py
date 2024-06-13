from Structure.Edge import Edge
from Structure.Node import Node
from Model.State import State
from Model.Action import Action

class Graph:
    """
    Representa un grafo con nodos y aristas, donde cada arista tiene una acción asociada.

    Atributos:
        nodes (dict): Un diccionario que almacena los nodos del grafo, donde las claves son los nombres de los estados y los valores son instancias de la clase Node.
    """    
    def __init__(self, grid=None):
        self.nodes = {}
        if grid:
            self.addNodesFromGrid(grid)
            self.addEdgesFromGrid(grid)

    def addNode(self, state):
        """
        Agrega un nodo al grafo.

        Args:
            state (State): El estado que representa el nodo a agregar.
        """        
        node = Node(state)
        self.nodes[state.name] = node

    def addEdge(self, source, target, action):
        """
        Agrega una arista al grafo entre dos nodos con una acción asociada.

        Args:
            source (State): El estado de origen de la arista.
            target (State): El estado de destino de la arista.
            action (Action): La acción asociada a la arista.
        """        
        if source.name not in self.nodes:
            self.addNode(source)
        if target.name not in self.nodes:
            self.addNode(target)
        edge = Edge(source, target, action)
        self.nodes[source.name].state.edges.append(edge)

    def addNodesFromGrid(self, grid):
        """
        Agrega nodos al grafo desde una cuadrícula.

        Args:
            grid (dict): Un diccionario que representa una cuadrícula con la configuración inicial de nodos.
        """        
        for key, value in grid.items():
            name = key
            is_goal = value['goal']
            is_deadend = value['deadend']
            heuristic = value['heuristic']
            state = State(name, is_goal, is_deadend, heuristic)
            self.addNode(state)

    def addEdgesFromGrid(self, grid):
        """
        Agrega aristas al grafo desde una cuadrícula.

        Args:
            grid (dict): Un diccionario que representa una cuadrícula con la configuración inicial de aristas.
        """        
        for key, value in grid.items():
            source_name = key
            source = self.nodes[source_name].state
            for adj in value['Adj']:
                target_name = adj['name']
                target = self.nodes[target_name].state
                actions = adj['A']
                for direccion, probabilidad in actions.items():
                    action = Action(direccion, probabilidad)
                    self.addEdge(source, target, action)

    def printNodes(self):
        """
        Imprime todos los nodos del grafo.
        """
        print("Nodos:")
        for name in self.nodes:
            print(name)

    def printEdges(self):
        """
        Imprime todas las aristas del grafo.
        """        
        print("Aristas:")
        for name, node in self.nodes.items():
            for edge in node.state.edges:
                print(f"Origen: {name}, Destino: {edge.target.name}, Accion: {edge.action}")

    def printEdgesById(self, name):
        """
        Imprime las aristas de un nodo específico del grafo.

        Args:
            name (str): El nombre del nodo cuyas aristas se desean imprimir.
        """        
        if name in self.nodes:
            print(f"Aristas del nodo {name}:")
            for edge in self.nodes[name].state.edges:
                print(f"Destino: {edge.target.name}, Accion: {edge.action}")
        else:
            print(f"No se encontró el nodo {name}")
