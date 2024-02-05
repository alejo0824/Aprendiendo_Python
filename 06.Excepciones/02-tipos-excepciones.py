# En Python, hay varios tipos de excepciones integradas que se utilizan para manejar
# situaciones específicas de error. Algunas de las excepciones más comunes incluyen:

# SyntaxError: Ocurre cuando hay un error de sintaxis en el código.
# Ejemplo de SyntaxError
# print "Hola, Mundo!"

# IndentationError: Se produce cuando hay un error en la indentación del código.
# Ejemplo de IndentationError
if True:
print("Indentación incorrecta")


# NameError: Ocurre cuando se intenta utilizar una variable que no ha sido definida.
# Ejemplo de NameError
print(variable_no_definida)

# TypeError: Se produce cuando se realiza una operación en un tipo de dato incorrecto.
# Ejemplo de TypeError
resultado = 10 + "5"

# ValueError: Ocurre cuando una función recibe un argumento del tipo correcto pero con un valor incorrecto.
# Ejemplo de ValueError
numero = int("abc")

# ZeroDivisionError: Se produce cuando intentamos dividir entre cero.
# Ejemplo de ZeroDivisionError
resultado = 10 / 0
