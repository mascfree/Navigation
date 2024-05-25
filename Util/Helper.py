import json


def leer_json(filename):
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
    
