# En Python puedes crear excepciones personalizadas, también conocidas como
# excepciones definidas por el usuario. Esto puede ser útil cuando deseas
# manejar situaciones específicas en tu código de manera más detallada
# y clara. Para definir una excepción personalizada, normalmente creas
# una nueva clase que herede de la clase base Exception o de una de
# sus subclases.

class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje="Este es un error personalizado."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def funcion_que_lanza_excepcion():
    # Algo va mal
    raise MiErrorPersonalizado("Ocurrió un problema en la función.")


try:
    funcion_que_lanza_excepcion()
except MiErrorPersonalizado as e:
    print(f"Se capturó una excepción personalizada: {e}")

# En este ejemplo, hemos creado la clase MiErrorPersonalizado que hereda
# de Exception. Hemos definido un método __init__ para personalizar el
# mensaje de la excepción y hemos llamado al constructor de la clase
# base con super().__init__(self.mensaje).

# Después, creamos una función llamada funcion_que_lanza_excepcion que
# lanza la excepción personalizada. En el bloque try, llamamos a esta
# función y capturamos la excepción MiErrorPersonalizado en el bloque
# except, donde imprimimos el mensaje de la excepción.

# Crear excepciones personalizadas puede hacer que tu código sea más
# legible y facilitar la identificación y el manejo de errores específicos
# en tu aplicación.
