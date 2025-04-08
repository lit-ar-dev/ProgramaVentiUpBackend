from ..datastore.json_store import JSONDataStore
from pathlib import Path


# Obtener la ruta absoluta del directorio que contiene config.py
ruta_actual = Path(__file__).resolve().parent

# Navegar hacia el directorio raíz del proyecto
ruta_proyecto = ruta_actual.parent.parent

# Construir la ruta a la carpeta 'json'
ruta_json = ruta_proyecto / 'json'

# Verificar si la carpeta 'json' existe
if ruta_json.exists() and ruta_json.is_dir():
    data_store = JSONDataStore(ruta_json)
else:
    raise Exception("La carpeta 'json' no existe.")