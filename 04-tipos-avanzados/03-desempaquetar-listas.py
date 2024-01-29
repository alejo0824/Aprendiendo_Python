""" realiza la asignación de variables para cada elemento de la lista numeros
y luego imprime los valores de las variables asignadas. 
A esto se le conoce como "desempaquetado"
 """
numeros = [1, 2, 3]

# Asignación de variables por cada elemento de la lista
primero, segundo, tercer = numeros
print(primero, segundo, tercer)

# ==================================================================================
# Para solo un elemento
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Otros es un iterable de un conjunto de datos que no conocemos
primero, segundo, *otros = numeros
print(primero, segundo,  otros)

# También puedo imprimir el ultimo elemento, penúltimo
primero, segundo, *otros, penu, ultimo = numeros
print(primero, segundo,  otros, penu, ultimo)
