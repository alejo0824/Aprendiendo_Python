# una tupla es una estructura de datos que se utiliza para almacenar una colección
# ordenada e inmutable de elementos. La principal característica de las tuplas es
# que no pueden ser modificadas una vez creadas, lo que las diferencia de las listas,
# que son mutables.

# Las tuplas se crean utilizando paréntesis () y pueden contener cualquier tipo de
# elemento, como números, cadenas de texto, booleanos, u otras tuplas.
# Creación de Tuplas
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Creación de una tupla → Se puede con cualquier iterable
punto = tuple([1, 2])
print("dd", punto[1])

# Características clave de las tuplas:

# Inmutabilidad: Una vez que se crea una tupla, no se pueden modificar sus elementos.
# No puedes agregar, eliminar o cambiar elementos en una tupla después de su creación.

# Indexación: Al igual que las listas, las tuplas son indexadas, lo que significa que
# puedes acceder a elementos individuales utilizando su posición en la tupla.

# Tupla de números
tupla_numeros = (1, 2, 3, 4, 5)

# Tupla de cadenas de texto
tupla_cadenas = ('a', 'b', 'c', 'd')

print(tupla_numeros[0])  # Output: 1
print(tupla_cadenas[2])  # Output: 'c'

# Longitud fija: La longitud de una tupla es fija y no puede cambiar después de su creación.

# Iterabilidad: Puedes iterar sobre los elementos de una tupla utilizando bucles for.

# Tupla mixta
tupla_mixta = (1, 'hello', True, 3.14)

for elemento in tupla_mixta:
    print(elemento)

# Se puede hacer los mismo que las listas con las tuplas MENOS MODIFICARLAS

menosNumeros = numeros[:2]
print(menosNumeros)

primero, segundo, * otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# ERROR → No se puede modificar
# numeros[0] = 5
