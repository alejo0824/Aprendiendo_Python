# numero = 1

# while numero < 100:  # Si se se cumple la condición del While, ejecuta el WHILE
#     print(numero)
#     numero *= 2


# en este código, sequira ejecutándose hasta que el usuario ingrese
# el comando "salir" (en cualquier combinación de mayúsculas y minúsculas)

comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)
