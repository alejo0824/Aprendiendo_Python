""" La función open() en Python se utiliza para abrir un archivo y obtener un objeto de 
archivo que puede utilizarse para leer o escribir en él. Se le pasa al menos un argumento, 
que es el nombre del archivo que se desea abrir. Además, puede especificar el modo de 
apertura, como "r" para lectura, "w" para escritura (creando un nuevo archivo o sobrescribiendo 
el existente), "a" para agregar contenido al final del archivo, etc. Una vez que se utiliza el 
archivo, es importante cerrarlo con el método close() para liberar los recursos del sistema 
operativo asociados con él """
from io import open

# ================================================ Escritura ================================================
# texto = "Hola mundo"

# archivo = open("09.archivos/archivo-prueba.txt", "w") # Modo escritura, si no existe, se crea
# archivo.write(texto)
# archivo.close() # Siempre se tiene que cerrar el archivo
# print(texto)

# ================================================= Lectura =================================================
# archivo = open("09.archivos/archivo-prueba.txt", "r") # por defeco es Read
# texto = archivo.read()
# archivo.close()
# print(texto)

# ============================================= Lectura como lista============================================
# archivo = open("09.archivos/archivo-prueba.txt", "r")  # por defeco es Read
# texto = archivo.readlines() # aquí es se convierte en lista
# archivo.close()
# print(texto)

# =========================================== Métodos mágicos ================================================
# Con with se cierra de forma automática (sin necesidad de usar close)
# with open("09.archivos/archivo-prueba.txt", "r") as archivo:
#     print(archivo.readlines())
#     # Este método es para volver a leer el archvio y ejecutar la línea de abajo
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# ============================================= Escribir en el ==============================================
# archivo = open("09.archivos/archivo-prueba.txt", "a+")
# archivo.write("Chao mundo :c")
# archivo.close()

# ============================================ Lectura y escritura============================================

with open("09.archivos/archivo-prueba.txt", "r+") as archivo:
    texto = archivo.readlines()  # Lista
    archivo.seek(0)
    texto[0] = "Chanchito Feliz la"
    archivo.writelines(texto)
