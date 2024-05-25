from Util.Helper import leer_json
from Estructura.Grafo import Grafo
from Modelo.Estado import Estado
from Modelo.Accion import Accion
from Modelo.MDP import MDP
import time
import psutil

def ejecutar_MDP(filename):
    # Cargar el archivo JSON
    estructura = leer_json(filename)

    # Crear grafo y agregar nodos
    grafo = Grafo()

    # Iterar sobre los elementos del JSON para agregar nodos al grafo
    for key, value in estructura.items():
        nombre = key
        es_meta = value['goal']
        es_mortal = value['deadend']
        heuristica = value['heuristic']
        estado = Estado(nombre, es_meta, es_mortal, heuristica)
        grafo.agregar_nodo(estado)

    # Iterar sobre los elementos del JSON para agregar aristas al grafo
    for key, value in estructura.items():
        origen_nombre = key
        origen = grafo.nodos[origen_nombre].estado
        for adj in value['Adj']:
            destino_nombre = adj['name']
            acciones = adj['A']
            for direccion, probabilidad in acciones.items():
                accion = Accion(direccion, probabilidad)
                grafo.agregar_arista(origen, Estado(destino_nombre), accion)

    mdp = MDP(grafo)

    # Obtener uso de la memoria antes de la ejecución
    memoria_inicial = psutil.virtual_memory().used

    # Obtener tiempo actual antes de la ejecución
    tiempo_inicial = time.time()

    # Ejecutar Iteración de Valor
    mdp.iteracion_de_valor()
    mdp.imprimir_valores()

    # Ejecutar Iteración de Política
    politica = mdp.iteracion_de_politica()
    mdp.imprimir_politica(politica)

    # Obtener tiempo actual después de la ejecución
    tiempo_final = time.time()

    # Obtener uso de la memoria después de la ejecución
    memoria_final = psutil.virtual_memory().used

    # Calcular tiempo transcurrido en segundos
    tiempo_transcurrido = tiempo_final - tiempo_inicial

    # Calcular uso de la memoria en megabytes
    memoria_utilizada_mb = (memoria_final - memoria_inicial) / (1024 * 1024)

    # Imprimir resultados
    print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")
    print(f"Uso de memoria: {memoria_utilizada_mb} MB")

# Ejecutar el primer caso de prueba
print("Ejecutando primer caso de prueba navigator3-15-0-0.json:")
ejecutar_MDP('Problema\\navigator3-15-0-0.json')

# Ejecutar el segundo caso de prueba
print("\nEjecutando segundo caso de prueba navigator4-10-0-0.json:")
ejecutar_MDP('Problema\\navigator4-10-0-0.json')
