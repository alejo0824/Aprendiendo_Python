# else y finally son bloques de código que pueden estar asociados con
# una declaración try y except para manejar excepciones.

# 1. else: El bloque else se ejecuta si no se produce ninguna excepción
# en el bloque try. Es decir, si el código dentro del bloque try
# se ejecuta sin lanzar ninguna excepción, el bloque else se ejecutará
# inmediatamente después.
try:
    # Código que podría generar una excepción
    resultado = 10 / 2
except ZeroDivisionError:
    print("¡Error! No puedes dividir por cero.")
else:
    # Se ejecuta si no se produce ninguna excepción
    print("La operación fue exitosa.")
# En este ejemplo, como la división no genera ninguna excepción,
# el bloque else se ejecutará y imprimirá "La operación fue exitosa".

# =====================================================================================

# 2.El bloque finally se ejecuta siempre, independientemente de si se produce una
# excepción o no. Esto significa que el código dentro del bloque finally se ejecutará
# sin importar si se maneja una excepción en el bloque except o si no se produce
# ninguna excepción en el bloque try.

try:
    # Código que podría generar una excepción
    resultado = 10 / 2
except ZeroDivisionError:
    print("¡Error! No puedes dividir por cero.")
else:
    # Se ejecuta si no se produce ninguna excepción
    print("La operación fue exitosa.")
finally:
    # Se ejecuta siempre, independientemente de si se produjo una excepción o no
    print("Esto se ejecutará sin importar qué.")

# En este ejemplo, tanto si se produce una excepción como si no, el bloque
# finally imprimirá "Esto se ejecutará sin importar qué."
# =====================================================================================

# En resumen, else se ejecuta cuando no hay excepciones en el bloque try, y finally
# se ejecuta siempre, independientemente de las excepciones. Ambos son opcionales y
# pueden usarse según las necesidades específicas de manejo de excepciones en tu código.
