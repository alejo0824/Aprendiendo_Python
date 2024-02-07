from pathlib import Path

path = Path("08.Rutas")
print(path.exists())  # Saber si existe
# Path.mkdir()  # Crear Directorio
# Path.rmdir() # Eliminar solo si la carpeta esta vacía
# Path.rename("Cancho-Feliz") # Renombrar el archivo

for p in path.iterdir():
    print(p)
