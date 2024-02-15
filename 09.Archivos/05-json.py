""" Para trabajar con JSON en Python, puedes usar el módulo incorporado json.
Este módulo proporciona funciones para codificar (serializar) objetos Python
en formato JSON y decodificar (deserializar) datos JSON en objetos Python """

import json
from pathlib import Path

# ======================================== Escribir JSON ========================================
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"},
# ]

# data = json.dumps(productos)
# Path("09.archivos/productos.json").write_text(data)

# =========================================== Leer JSON ===========================================
data = Path("09.archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)


# ======================================== Modificar JSON ========================================
productos[0]["name"] = "chanchito Feliz"
Path("09.archivos/productos.json").write_text(json.dumps(productos))
