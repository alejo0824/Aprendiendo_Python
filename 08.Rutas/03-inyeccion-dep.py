# Se utiliza para crear componentes de software que son altamente modulares, desacoplados y fáciles de probar.

""" import usuario

# Sin inyección de dependecia


def guardar():
    usuario.guardar()

# Con inyección de dependencias, Podemos guardar cualquier cosa que no sea usuario (productos, PQR, etc)


def guardar(entidad):
    entidad.guardar()
 """

# NOTA: Se tiene que ejecutar en VS desde la carpeta 08.rutas, es decir solo debe estar la carperta 08.rutas
#   Desde terminal: cd 08.rutas luego code .

from pathlib import Path

path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "Base de datos",
    "api": "Esta es al api",
    "graphql": "Esto es graphql"
}


def load(p):
    # Importar paquetes y modulos de manera dinamica
    paquete = __import__(str(p).replace("/", "."))
    try:
        # Imprimiendo lo que hay dentro del los __init__ de las carpetas
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene la fución de init")


list(map(load, paths))
