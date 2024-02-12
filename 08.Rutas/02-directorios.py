from pathlib import Path

path = Path("08.Rutas")
# print(path.exists())  # Saber si existe
# Path.mkdir()  # Crear Directorio
# Path.rmdir() # Eliminar solo si la carpeta esta vacía
# Path.rename("Cancho-Feliz") # Renombrar el archivo

archivos = [p for p in path.iterdir() if not p.is_dir()]

# Todos los que terminen con extención py
archivos = [p for p in path.glob("*.py")]

# Todos los que terminen con extención py y empiece con "01-"
archivos = [p for p in path.glob("01-*.py")]

# todos las rutas que tengan .py de manera recursiva, también
# se puede con la función rglob si no nos gustas los astericos
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
