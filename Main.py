from Utils.Helper import readJson
from Structure.Graph import Graph
from Algorithms.IV import IV
from Algorithms.IP import IP

def ejecutar_MDP(filename,number_problem):
    # Cargar el archivo JSON
    grid = readJson(filename)

    # Crear grafo
    graph = Graph(grid, number_problem)

    # Ejecutar iteración de politica
    IP(graph, gamma=0.99, threshold=0.001, standard_cost=1, deadend_cost=1).print1()

    # Ejecutar iteración de valor
    IV(graph, gamma=0.99, threshold=0.001, standard_cost=1, deadend_cost=1).print1()    


print("======================= navigator3-15-0-0.json =======================")
ejecutar_MDP('Problems/navigator3-15-0-0.json',1) 

print("======================= navigator4-10-0-0.json =======================")
ejecutar_MDP('Problems/navigator4-10-0-0.json',2)