lista1 = [1, 2, 3, 4]

# print(*lista1)  # Imprimir los elementos como argumento
# def n(n1, n2, n3, n4):
# print(n1 + n2 + n3 + n4)
# n(*lista)

lista2 = [5, 6]

combinada = ["hola", *lista1, "mundo", *lista2]
print(combinada)

print("---------------------------")

# Con diccionarios

punto1 = {"x": 19, "y": "Hola"}
punto2 = {"y": 15}

# Si encuentra una llave repetida, la remplaza
nuevoPunto = {**punto1, "lala": "Hola Mundo", **punto2, "z": 45}
print(nuevoPunto)  # Creamos un nuevo diccionario
