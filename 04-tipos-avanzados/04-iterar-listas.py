# En Python, puedes iterar sobre listas de varias maneras. Aquí te presento algunas de las formas más comunes:

# ================================ Método 1: Utilizando un Bucle for ============================================
# El bucle for es una forma común de iterar sobre los elementos de una lista:

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)

# ================================ Método 2: Utilizando la Función enumerate() ================================
# La función enumerate() te permite obtener tanto el índice como el valor de cada elemento de la lista:

frutas = ["manzana", "banana", "cereza"]

for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")
# Esto imprimirá tanto el índice como la fruta en cada iteración.

# ================================ Método 3: Utilizando un Bucle while =========================================
# También puedes utilizar un bucle while para iterar sobre los elementos de una lista:

frutas = ["manzana", "banana", "cereza"]

indice = 0
while indice < len(frutas):
    print(frutas[indice])
    indice += 1
