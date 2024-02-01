""" La anulación de método (o "overriding" en inglés) se refiere a la capacidad 
de una clase derivada (subclase) de proporcionar una implementación diferente 
para un método que ya está definido en su clase base (superclase). 
En otras palabras, la anulación de método permite que una subclase proporcione 
su propia implementación de un método que ya existe en la clase base.

Cuando una subclase define un método con el mismo nombre y la misma 
firma (parámetros) que un método en la clase base, se dice que ha anulado 
ese método. La anulación de método es una parte fundamental 
del <polimorfismo> en la programación orientada a objetos (OOP). """


class Animal:
    def hacer_sonido(self):
        print("Sonido genérico de un animal")


class Gato(Animal):
    def hacer_sonido(self):
        print("¡Miau!")


class Perro(Animal):
    def hacer_sonido(self):
        print("¡Guau!")


# Crear instancias de las subclases
gato = Gato()
perro = Perro()

# Llamar al método haciendo_sonido de cada instancia
gato.hacer_sonido()  # Imprime "¡Miau!"
perro.hacer_sonido()  # Imprime "¡Guau!"


# La clase Animal tiene un método hacer_sonido que proporciona una
# implementación genérica.
# Las clases Gato y Perro son subclases de Animal y anulan el método
# hacer_sonido para proporcionar sus propias implementaciones específicas.

# La anulación de método es una herramienta poderosa que permite que
# las subclases proporcionen comportamientos específicos sin cambiar
# la interfaz de la clase base. Esto promueve la flexibilidad y
# la extensibilidad en el diseño de clases en la programación orientada a objetos.
