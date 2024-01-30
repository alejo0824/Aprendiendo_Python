# Un Set (Conjunto) es una estructura de datos que representa una colección desordenada
# y sin duplicados de elementos. Los conjuntos son similares a las listas y tuplas,
# pero tienen características específicas que los distinguen:

# Elementos Únicos: Un conjunto no puede contener elementos duplicados. Si intentas
# agregar un elemento que ya está presente en el conjunto, no se producirán duplicados.

# Desordenados: Los elementos en un conjunto no tienen un orden específico. No puedes
# acceder a elementos individuales por índice, ya que los conjuntos no tienen índices.

# Mutables: A diferencia de las tuplas, los conjuntos son mutables, lo que significa
# que puedes agregar o eliminar elementos después de la creación del conjunto.

# Sintaxis: Los conjuntos se crean utilizando llaves {} o la función set().

# Crear un conjunto con llaves
conjunto1 = {1, 2, 3, 4, 5}

# Crear un conjunto con la función set()
conjunto2 = set([3, 4, 5, 6, 7])

# Conjunto con elementos mixtos
conjunto_mixto = {1, 'hello', 3.14, True}

# Conjunto vacío
conjunto_vacio = set()

# ======================================= Algunas Funciones de los Sets =======================================

# Creación del SET <primero>
# Eliminará los elementos duplicados  el 1 y el 2 ya que no se puede duplicar el elemento
primero = {1, 1, 2, 2, 3, 4}
primero.add(5)
primero.remove(1)

segundo = [3, 4, 5]
segundo = set(segundo)  # Se puede transformar cualquiere iterable a SET

# • Agregar elementos:
conjunto1.add(6)

# • Eliminar elementos:
conjunto2.remove(3)

# • Operaciones de conjuntos (unión, intersección, diferencia, diferencia simétrica (XOR)):

#  - Union
union = conjunto1.union(conjunto2)
print(primero | segundo)  # Unir dos set y ya elimina los elementos duplicados

#  - Intersección
interseccion = conjunto1.intersection(conjunto2)
print(primero & segundo)  # Trae los elementos en común

# - Diferencia
diferencia = conjunto1.difference(conjunto2)
print(primero - segundo)

#  - diferencia simétrica (XOR)
print(primero ^ segundo)


# Verificación de pertenencia:
pertenece = 4 in conjunto1
