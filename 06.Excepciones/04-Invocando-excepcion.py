# Se puede invocar (lanzar) excepciones manualmente utilizando la palabra clave
# <raise>. Puedes utilizar raise con o sin argumentos para crear y lanzar excepciones.

def division(n=0):
    if n == 0:
        raise ZeroDivisionError(
            "No se puede dividir por 0", f"Valor de n: {n}")
    return 5 / n


try:
    division()
except ZeroDivisionError as e:
    print(e)

# En este ejemplo, la función division toma un argumento n por defecto establecido en 0.
# Si n es igual a 0, se lanza una excepción ZeroDivisionError con un mensaje
# personalizado que incluye el valor de n. Luego, en el bloque try, intentamos llamar a
# la función division() sin proporcionar un valor para n. Como n tiene el valor por defecto
# de 0, se lanza la excepción, y luego es capturada y manejada en el bloque except,
# donde se imprime el mensaje de error.
