mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])  # Imprimir un elemento. Los indices empiezan con 0
# Modificando un elemento, en este caso el primer elemento
mascotas[0] = "Bicho"
print(mascotas)

print(mascotas[:3])  # Imprimir los tres primeros elementos
print(mascotas[2:])  # Desde donde quiero imprimer

# Se invierte la forma de imprimir, como esta en -1 imprime el último elemento
# de la lista, si fuera -2 sería el penúltimo
print(mascotas[-1])
# Imprime los elementos [0] [2] [4], wl número a la izquierda de los :: se
# le indica desde donde comenzar
print(mascotas[::2])

# EJEMPLO PARA USAR - imprimir los pares
numeros = list(range(21))
print(numeros[1::2])

# opcion 2 para imprimir elementos impares
numeros = list(range(1, 21))
print(numeros[::2])
