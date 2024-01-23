# la instrucción for se utiliza para realizar iteraciones sobre secuencias
# como listas, tuplas, cadenas de texto, diccionarios o elementos iterables.
# El bucle for permite ejecutar un bloque de código repetidamente, una vez
# para cada elemento de la secuencia.

# La sintaxis básica de un bucle for en Python es la siguiente:

# for variable in secuencia:
# Código que se ejecutará en cada iteración

# Ejemplo
for numero in range(5):
    print(numero, numero * 'hola mundo ')

# ===========================FOR ELSE===========================
# el bucle for puede tener una cláusula else que se ejecuta
# cuando la iteración se completa sin encontrar un break.
# La sintaxis general es la siguiente:

# for variable in secuencia:
    # Código que se ejecutará en cada iteración
# else:
    # Código que se ejecutará al finalizar el bucle (si no se ha ejecutado un break)

# Ejemplo
buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:  # Sí el break no llega dentro del IF
    print("No enecotre el núemro buscado :c")


# Otro Iterable
for char in "Python":
    print(char)
