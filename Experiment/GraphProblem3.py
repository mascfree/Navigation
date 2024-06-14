import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos al grafo
nodes = range(1, 17)
G.add_nodes_from(nodes)

# Añadir aristas al grafo
edges = [
(1, 1),
(1, 5),
(1, 2),
(2, 2),
(2, 1),
(2, 3),
(2, 6),
(3, 3),
(3, 2),
(3, 4),
(3, 7),
(4, 4),
(4, 3),
(4, 8),
(5, 1),
(5, 5),
(5, 9),
(5, 6),
(6, 2),
(6, 5),
(6, 10),
(6, 7),
(7, 3),
(7, 6),
(7, 11),
(7, 8),
(8, 4),
(8, 7),
(8, 12),
(8, 8),
(9, 5),
(9, 9),
(9, 13),
(9, 10),
(10, 6),
(10, 9),
(10, 14),
(10, 11),
(11, 7),
(11, 10),
(11, 15),
(11, 12),
(12, 8),
(12, 11),
(12, 16),
(12, 12),
(13, 9),
(13, 13),
(13, 14),
(14, 10),
(14, 13),
(14, 14),
(14, 15),
(15, 11),
(15, 14),
(15, 15),
(15, 16),
(16, 12),
(16, 15),
(16, 16)
]

G.add_edges_from(edges)

# Definir las posiciones de los nodos en un diseño de columnas
pos = {}
for i in range(1, 17):
        col = (i - 1) % 4
        row = (i - 1) // 4
        pos[i] = (col, -row)

# Dibujar el grafo
plt.figure(figsize=(15, 10))
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='black', edgecolors='black', linewidths=0)
nx.draw_networkx_labels(G, pos, font_size=12, font_color='white')
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=15, edge_color='black')

# Mejorar el diseño visual
plt.title("Graph Problem Navegation - Prueba.json (De Carlos)", fontsize=16)
plt.axis('off')  # Ocultar los ejes

# Mostrar la gráfica
plt.show()
