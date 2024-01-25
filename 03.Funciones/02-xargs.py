"""permite recibir un número variable de argumentos.Estos argumentos se agrupan
en una tupla, en este caso llamada en una tupla llamada <numeros>. La función
luego itera sobre esta tupla y suma todos los valores, imprimiendo el resultado final. """


def suma(*numeros):  # con *<parametro> es una tupla y se comporta como un iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


# En cada llamada a la función suma, puedes proporcionar un número variable de argumentos,
# y la función los sumará todos. La función se adapta para manejar cualquier cantidad de argumentos que le pases.

suma(1, 2, 3)  # Resultado: 6
suma(4, 5, 6, 7)  # Resultado: 22
suma(10, 20, 30, 40, 50)  # Resultado: 150
