# Funciones conocidas ya implementadas en Py
print("La función print imprim algo en consola ")

# Una función es un bloque de código reutilizable que realiza una tarea e
# specífica. Las funciones permiten organizar el código de manera modular,
# lo que facilita la comprensión y el mantenimiento del programa. Una función
# en Python se define utilizando la palabra clave def, seguida del nombre
# de la función y paréntesis que pueden contener los parámetros de entrada


def hola():  # Crear mi función → def <nombre_funcion()> : (va identado)
    print("Hola Mundo!")
    print("Python")


hola()  # Ejecutando la función
hola()  # Se puede ejecutar múltiples veces


def hola2(nombre, apellido):  # Función con parametros
    print(f"Bienvenido {nombre} {apellido}")


# Usando una función con argumentos(valor que le estoy pasando)
hola2("Alejandro", "Tellez")
hola2("Chanchito", "Feliz")
# =======================================Argumentos Opcionales=======================================

# Los argumentos opcionales son parámetros que tienen un valor predeterminado
# asignado en la definición de la función. Esto significa que, si no se
# proporciona un valor al llamar a la función, se utilizará el valor
# predeterminado. Aquí hay un ejemplo:


def hola_parametro_opcional(nombre, apellido="Feliz"):
    print(f"Bienvenido {nombre} {apellido}")


hola_parametro_opcional("Alejandro", "Tellez")
hola_parametro_opcional("Chanchito")

# =======================================Argumentos Nombrados=======================================

# Los argumentos nombrados permiten pasar valores a una función utilizando
# el nombre del parámetro al que se le desea asignar un valor. Esto mejora la
# legibilidad y flexibilidad de las llamadas a funciones, especialmente
# cuando una función tiene muchos parámetros. Aquí hay un ejemplo:


def calcular_precio(total, descuento=0, impuestos=0):
    """
    Esta función calcula el precio final teniendo en cuenta descuentos e impuestos.
    """
    return total - descuento + impuestos


# Ejemplo de llamada a la función con argumentos nombrados (en desorden a la función)
precio_final = calcular_precio(descuento=10, total=100,  impuestos=5)

print(f"Precio final: {precio_final}")  # Salida: "Precio final: 95"
