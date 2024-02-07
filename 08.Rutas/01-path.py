""" Se puede trabajar con rutas y directorios utilizando el módulo <<pathlib>>. 
Estos módulos proporcionan funciones y clases para manipular rutas de archivos 
y directorios de manera fácil y eficiente. Aquí te doy una breve descripción 
de cómo puedes usarlos: """

# El módulo pathlib proporciona una interfaz orientada a objetos para
# trabajar con rutas y directorios.

from pathlib import Path

# Crear un objeto Path
ruta = Path("carpeta/subcarpeta/archivo.txt")

# El prefijo "r" es para evitar la interpretación especial de los caracteres como \.
Path(r"C:\Archivos de Programa\LOL")

# Crear una ruta absoluta
Path("C:/Archivos de Programa/LOL")

# Crear una ruta relativa
Path("carpeta/subcarpeta/archivo.txt")

Path = Path("hola-mundo/mi-archivo.py")

# ======= Metodos Utilies =======
Path.is_file()
Path.is_dir()
Path.exists()

# Propiedades
print(
    Path.name,  # Nombre de archivo con extensión
    Path.stem,  # Nombre de archivo SIN extensión
    Path.suffix,  # Solo la extención
    Path.parent,  # Direcotrio Padre
    Path.absolute()  # La ruta completa
)

p = Path.with_name("chanchito.exec")  # Para cambiar el nombre
print(p)

p = Path.with_suffix(".bat")  # Para cambiar la extesión
print(p)

p = Path.with_stem("feliz")  # Para cambiar el nombre sim su extensión
print(p)
