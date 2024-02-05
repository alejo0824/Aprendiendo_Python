""" En Python, una excepción es un evento anormal que ocurre durante la ejecución de un
programa y que interrumpe el flujo normal de ejecución. Cuando se produce una excepción,
el programa se detiene y se busca un bloque de código diseñado para manejar esa 
excepción específica. Estos bloques de código se llaman "manejadores de excepciones"."""

# Se puede manejar excepciones utilizando las sentencias <try>, <except>, <else> y <finally>
try:
    # Código que podría generar una excepción
    resultado = 10 / 0  # Intentando dividir por cero
except ZeroDivisionError:
    # Manejar la excepción específica
    print("¡Error! No puedes dividir por cero.")
else:
    # Se ejecuta si no se produce ninguna excepción
    print("La operación fue exitosa.")
finally:
    # Se ejecuta siempre, independientemente de si se produjo una excepción o no
    print("Esto se ejecutará sin importar qué.")
