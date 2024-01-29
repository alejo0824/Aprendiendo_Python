"""una lista es un tipo de dato que se utiliza para almacenar una 
colección ordenada de elementos. Puedes considerar una lista como 
una secuencia mutable de objetos. Los elementos en una lista pueden 
ser de diferentes tipos, como números, cadenas, booleanos, u otros 
objetos, incluso otras listas."""

mi_lista = [1, 2, 3, 'cuatro', 5.0, True]  # Creación básica de una lista

numeros = [1, 2, 3]
letras = ["a", "b", "c"]
palabras = ["Chanchito", "Feliz"]
palabrasFelices = ["Chanchito", "Feliz", "Felipe", "Python"]
booleans = [True, False, False, True]
matriz = [[0, 1], [1, 0]]

# contiene 10 elementos, y cada elemento es el número 0. En otras palabras,
# la lista ceros está compuesta por 10 repeticiones del valor 0.
ceros = [0] * 10

alfanumericos = numeros + letras  # Concatenar dos listas en una lista

rango = list(range(1, 11))  # Creación de una lista del 1 al 10

# Convierte la cadena de texto "Hola Mundo" en una lista de caracteres.
chars = list("Hola Mundo")
print(chars)
