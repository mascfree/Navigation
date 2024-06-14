Descripción de Archivos
--------------------------------------------------------------------------------
main.py
El archivo principal para ejecutar el proyecto y mostrar los resultados.

Utils/Helper.py
Contiene decoradores y funciones de utilidad, como la medición del rendimiento.

Structure/Node.py
Define la clase Node, que representa un nodo en el grafo.

Structure/Edge.py
Define la clase Edge, que representa una arista en el grafo.

Model/State.py
Define la clase State, que representa el estado de un nodo en el grafo.

Model/Action.py
Define la clase Action, que representa una acción en el grafo.

Graph.py
Define la clase Graph, que representa el grafo completo y proporciona métodos para añadir nodos y aristas desde una cuadrícula.

IP.py
Implementa el algoritmo de Iteración de Políticas.

IV.py
Implementa el algoritmo de Iteración de Valores (Value Iteration).

Experiment/GraphProblem1.py
Dibuja el Grafo del problema navigator3-15-0-0.json con la librería networkx, se usó previamente 
GenParesAristasP1.py para generar la lista de pares de aristas que genera el dibujo del grafo.

GraphProblem2.py
Dibuja el Grafo del problema navigator4-10-0-0.json con la librería networkx, se usó previamente 
GenParesAristas2.py para generar la lista de pares de aristas que genera el dibujo del grafo.

Librerías Utilizadas:
---------------------------------------------------------------
json, psutil, time, functools, networkx, pandas

Ejecutado con Python 3.12.3

14/06
Nota: Para visualizar mejor las soluciones de ambos problemas se añadió un método print1, que 
permita visualizar la solución mas legible.





