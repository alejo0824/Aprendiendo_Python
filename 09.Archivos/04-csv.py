""" Para trabajar con archivos CSV en Python, puedes utilizar el módulo csv,
que proporciona funcionalidades para leer y escribir archivos CSV de manera sencilla. """

import csv
import os

# NOTA:  Todo csv se lee como string, no importa si se escribe o escribió números
# Modo de lectura ("r") y modo de escritura ("w").
# ====================================================== Escribir ======================================================
# newline='' es para que no coloque enters
# with open("09.archivos/archivo-prueba.csv", "w", newline='') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["Twit_id", "user_id", "Text"])
#     writer.writerow([1000, 1, "Este es mi Twit"])
#     writer.writerow([1002, 2, "Otro Twit!"])

# ======================================================== Leer ======================================================
# with open("09.archivos/archivo-prueba.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)

# ================================================== Actualizar CSV ==================================================
# Para actualizar un línea de un csv, es necesario crear una copia del archivo original.
with open("09.archivos/archivo-prueba.csv") as r, open("09.archivos/archivo_temp.csv", "w", newline='') as w:
    # Leemos del archivo original que contiene todos los datos
    reader = csv.reader(r)
    # Escribimos en un archivo temporal que está vacío al inicio
    writer = csv.writer(w)

    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "Este es mi Twit MODIFICADO 2"])
        else:
            writer.writerow(linea)

# Esto no funciona dentro del with en windows por eso se identa al mismo nivel de la función **with**
os.remove("09.archivos/archivo-prueba.csv")
os.rename("09.archivos/archivo_temp.csv", "09.archivos/archivo-prueba.csv")
