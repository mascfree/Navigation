from Utils.Helper import readJson
from Structure.Graph import Graph
from Algorithms.IV import IV
from Algorithms.IP import IP

def ejecutar_MDP(filename):
    # Cargar el archivo JSON
    grid = readJson(filename)

    # Crear grafo
    graph = Graph(grid)

    # Ejecutar iteración de politica
    IP(graph, gamma=0.8, threshold=0.05, standard_cost=1, deadend_cost=1).print()

    # Ejecutar iteración de valor
    IV(graph, gamma=0.8, threshold=0.05, standard_cost=1, deadend_cost=1).print()    


print("======================= navigator3-15-0-0.json =======================")
ejecutar_MDP('Problems/navigator3-15-0-0.json') 

print("======================= navigator4-10-0-0.json =======================")
ejecutar_MDP('Problems/navigator4-10-0-0.json')