# La instrucción if en Python se utiliza para ejecutar un bloque
# de código si una condición es verdadera. La sintaxis básica
# de la instrucción if es la siguiente:

edad = 15

if edad > 54:
    print('Puede ver la película con descuento')
    # La instrucción elif se utiliza para evaluar múltiples condiciones después
    # de la condición inicial del if. Puedes tener múltiples bloques elif seguidos de un bloque else al final
elif edad > 17:
    print("Puedes ver la película")
else:
    print('No puedes entrar')
    print("Ve a otro lado")
print('Todo bien  todo bonito')
