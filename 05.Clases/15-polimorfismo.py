# El polimorfismo permite que objetos de diferentes clases respondan a
# un mismo método o acción de manera específica a su propia implementación.
# En otras palabras, se refiere a la capacidad de un objeto de tomar
# muchas formas, donde un método puede comportarse de manera diferente según
# el tipo de objeto al que pertenece


from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"


class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"


class Pajaro(Animal):
    def hacer_sonido(self):
        return "¡Pío!"

# Función que utiliza polimorfismo


def hacer_ruido(animal):
    return animal.hacer_sonido()


# Crear instancias de las subclases
perro = Perro("Buddy")
gato = Gato("Whiskers")
pajaro = Pajaro("Tweety")

# Utilizar polimorfismo en la función hacer_ruido
print(hacer_ruido(perro))  # Imprime "¡Guau!"
print(hacer_ruido(gato))   # Imprime "¡Miau!"
print(hacer_ruido(pajaro))  # Imprime "¡Pío!"
