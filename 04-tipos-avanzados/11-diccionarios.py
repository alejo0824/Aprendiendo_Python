# Un diccionario es una estructura de datos que permite almacenar
# pares clave-valor. Es una colección mutable, desordenada y sin
# duplicados de elementos, donde cada elemento consiste en una clave
# única y su valor correspondiente. Los diccionarios son conocidos por
# su eficiencia en la búsqueda y recuperación de valores basándose en las claves.

# La sintaxis básica para crear un diccionario es mediante llaves {}
# y proporcionar pares clave-valor separados por comas.
mi_diccionario = {"clave1": "valor1", "clave2": "valor2", "clave3": "valor3"}

# En este ejemplo, "clave1", "clave2", y "clave3" son las claves, y "valor1",
# "valor2", y "valor3" son los valores correspondientes.

# ====================== Características clave de los diccionarios en Python: ======================

# 1. Mutabilidad: Los diccionarios son mutables, lo que significa que puedes agregar,
# modificar o eliminar elementos después de su creación.

# 2.Claves Únicas: Las claves en un diccionario son únicas. No puede haber dos
# claves idénticas en un mismo diccionario.

# 3. Acceso por Clave: Puedes acceder a los valores de un diccionario
# utilizando las claves. Por ejemplo:

valor = mi_diccionario["clave1"]

# Métodos Útiles: Los diccionarios en Python proporcionan una variedad de métodos útiles,
# - como keys() para obtener una lista de claves
# - values() para obtener una lista de valores
# - items() para obtener pares clave-valor como tuplas.

claves = mi_diccionario.keys()
valores = mi_diccionario.values()
pares = mi_diccionario.items()

print(claves)
print(valores)
print(pares)


# Forma como imprimir todos los registros del usuario
punto = {"x": 25, "y": 50}
print(punto)

# Se pueden añadir nuevos valores
punto["z"] = 45

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():  # Por Tuplas
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)
