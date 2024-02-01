class Pato:
    def nadar(self):
        print("El pato nada en el agua")


class Persona:
    def nadar(self):
        print("La persona nada en la piscina")


def hacer_nadar(objeto):
    objeto.nadar()


# Creamos instancias de las clases
pato = Pato()
persona = Persona()

# Llamamos a la función hacer_nadar con diferentes tipos de objetos
hacer_nadar(pato)     # Imprime: El pato nada en el agua
hacer_nadar(persona)  # Imprime: La persona nada en la piscina

# En este ejemplo, tenemos dos clases, Pato y Persona, cada una con un método nadar
# . Luego, tenemos una función llamada hacer_nadar que toma un objeto como
# parámetro y llama al método nadar de ese objeto.

# Aunque las clases Pato y Persona son diferentes y no comparten una jerarquía común,
# ambas pueden ser pasadas a la función hacer_nadar porque ambas tienen
# un método llamado nadar. Esto es un ejemplo de duck typing en acción:
# nos preocupamos por el comportamiento
# (en este caso, la capacidad de nadar) en lugar del tipo específico del objeto.
