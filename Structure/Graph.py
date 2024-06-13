from Structure.Edge import Edge
from Structure.Node import Node
from Model.State import State
from Model.Action import Action

class Graph:
    def __init__(self, grid=None):
        self.nodes = {}
        if grid:
            self.addNodesFromGrid(grid)
            self.addEdgesFromGrid(grid)

    def addNode(self, state):
        node = Node(state)
        self.nodes[state.name] = node

    def addEdge(self, source, target, action):
        if source.name not in self.nodes:
            self.addNode(source)
        if target.name not in self.nodes:
            self.addNode(target)
        edge = Edge(source, target, action)
        self.nodes[source.name].state.edges.append(edge)

    def addNodesFromGrid(self, grid):
        for key, value in grid.items():
            name = key
            is_goal = value['goal']
            is_deadend = value['deadend']
            heuristic = value['heuristic']
            state = State(name, is_goal, is_deadend, heuristic)
            self.addNode(state)

    def addEdgesFromGrid(self, grid):
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
        print("Nodos:")
        for name in self.nodes:
            print(name)

    def printEdges(self):
        print("Aristas:")
        for name, node in self.nodes.items():
            for edge in node.state.edges:
                print(f"Origen: {name}, Destino: {edge.target.name}, Accion: {edge.action}")

    def printEdgesById(self, name):
        if name in self.nodes:
            print(f"Aristas del nodo {name}:")
            for edge in self.nodes[name].state.edges:
                print(f"Destino: {edge.target.name}, Accion: {edge.action}")
        else:
            print(f"No se encontró el nodo {name}")
