import json
import psutil
import time
from functools import wraps


def readJson(filename):
    """
    Lee un archivo JSON y carga su contenido en un diccionario.

    Args:
        filename (str): El nombre del archivo JSON que se va as leer.

    Returns:
        dict: Un diccionario que contiene los datos del archivo JSON.

    Raises:
        FileNotFoundError: Si el archivo especificado no se encuentra.
        json.JSONDecodeError: Si hay un error al decodificar el archivo JSON.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"El archivo '{filename}' no se encontró.")
        return None
    
def get_memory_usage():
    # Obtener la memoria utilizada por el proceso actual
    process = psutil.Process()
    return process.memory_info().rss

def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Tomar varias muestras de memoria inicial
        memoria_inicial_samples = [get_memory_usage() for _ in range(5)]
        memoria_inicial = sum(memoria_inicial_samples) / len(memoria_inicial_samples)
        
        tiempo_inicial = time.time()

        result = func(*args, **kwargs)

        tiempo_final = time.time()

        # Tomar varias muestras de memoria final
        memoria_final_samples = [get_memory_usage() for _ in range(5)]
        memoria_final = sum(memoria_final_samples) / len(memoria_final_samples)

        tiempo_transcurrido = (tiempo_final - tiempo_inicial) * 1000  # Convertir a milisegundos
        memoria_utilizada_mb = max(0, (memoria_final - memoria_inicial) / (1024 * 1024))

        print(f"Tiempo transcurrido: {tiempo_transcurrido:.2f} milisegundos")
        print(f"Memoria utilizada: {memoria_utilizada_mb:.2f} MB")

        return result
    return wrapper

