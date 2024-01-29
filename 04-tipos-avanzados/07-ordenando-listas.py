numeros = [1, 54, 2, 6, 89, 74, 12, 11, 25]

numeros.sort()  # Ordena de forma ASC
numeros.sort(reverse=True)  # Ordena de forma DESC

numeros2 = sorted(numeros)  # Crea una nueva lista Ordena de forma ASC
numeros2 = sorted(numeros, reverse=True)

print(numeros)
print(numeros2)

usuarios = [
    ["Chancho", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

usuarios.sort()  # Con una lista de lista o tuplas solo se puede si el primer elemento es el que queremos ordenar


def ordena(elemento):
    return elemento[1]


# La función key se aplica a cada elemento de la lista antes de realizar la comparación
# para determinar el orden. Esto permite personalizar el proceso de ordenación en
# función de algún criterio específico.

usuarios.sort(key=ordena, reverse=True)  # En este caso el segundo valor


# una función lambda es una función anónima y pequeña definida con la palabra clave lambda.
# Este tipo de funciones son útiles cuando necesitas una función rápida para un corto período
# de tiempo y no quieres definir una función completa con la palabra clave def. La sintaxis general
# de una función lambda es la siguiente:

# lambda argumentos: expresion

# Lo mismo que la línea 21 hasta la 29
usuarios.sort(key=lambda elemento: elemento[1], reverse=True)
print(usuarios)
