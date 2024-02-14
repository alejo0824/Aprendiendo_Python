from pathlib import Path

# para mostrar la información sobre los tiempos de acceso, creación y modificación de un archivo.
from time import ctime

archivo = Path("09.Archivos/archivo-prueba.txt")
# archivo.exists() # Para saber si existe el archivo
# archivo.rename() # Para renombrar el archivo
# archivo.unlink() # Para eliminar el archivo

# print(archivo.stat()) # estadisticas

# mprime la fecha y hora del último acceso (st_atime) del archivo utilizando la función ctime()
# para convertir el tiempo en un formato legible para humanos.
print("Acceso", ctime(archivo.stat().st_atime))

# Imprime la fecha y hora de creación (st_ctime) del archivo utilizando ctime().
print("creacioón", ctime(archivo.stat().st_ctime))

# Imprime la fecha y hora de la última modificación (st_mtime) del archivo utilizando ctime().
print("modificación", ctime(archivo.stat().st_mtime))
