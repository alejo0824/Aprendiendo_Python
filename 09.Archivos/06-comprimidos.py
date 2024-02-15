""" Para trabajar con archivos comprimidos en Python, puedes utilizar el módulo zipfile, 
que te permite crear, leer y extraer archivos ZIP, así como también puedes utilizar 
el módulo tarfile para archivos tar.  """

from pathlib import Path
from zipfile import ZipFile, BadZipFile

# ============================= Comprimir los archivos =============================
# with ZipFile("09.archivos/comprimidos.zip", "w") as zip:

#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "09.archivos/comprimidos.zip":
#             zip.write(path)

# ============================= Leer los archivos Comprimidos =============================

archivo = Path("09.Archivos/comprimidos.zip")

with ZipFile("09.Archivos/comprimidos.zip") as zf:
    print(zf.namelist())

    info = zf.getinfo("09.Archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size
    )

    # Descomprimir la información
    zf.extractall("09.Archivos/descomprimidos")
