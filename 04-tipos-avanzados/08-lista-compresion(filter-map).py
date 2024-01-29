usuarios = [
    ["Chancho", 4],
    ["Felipe", 1],
    ["Pulga", 5]
]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# Lo mismo que esta arriba ↑ Esto es MAP

# La función "map" aplica una función a cada elemento de una secuencia y devuelve
# un iterador con los resultados. La sintaxis es la siguiente:
# map(funcion, secuencia)
# • funcion: La función que se aplicará a cada elemento de la secuencia.
# • secuencia: La secuencia de entrada.

# En este caso solo devolverá el primer elemento (los nombres)
nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# Filtrar eso es Filter
# La función filter filtra los elementos de una secuencia basándose en una condición
# dada y devuelve un iterador con los elementos que cumplen dicha condición.
# La sintaxis es la siguiente:
# filter(condicion, secuencia)
# • condicion: La condición que se aplica a cada elemento de la secuencia. Solo se incluyen
#   los elementos que cumplen esta condición.
# •secuencia: La secuencia de entrada.

# filtra y retorna los IDde los nombres mayores a 2
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)


# ======================= Funciones MAP y Filter con funciones Lambda =======================

# MAP
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# Filter
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
