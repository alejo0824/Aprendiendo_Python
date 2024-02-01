class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        # hay una convención que se utiliza para indicar que un atributo o método
        # debe tratarse como "privado". Esta convención consiste en añadir un guion
        # bajo como prefijo al nombre del atributo o método
        self.__nombre = nombre
        self.edad = edad

# ================ Para retornar o modificar propiedades privadas más adelantes ================

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre
# ================================================================================================

    def habla(self):
        print(f"{self.__nombre} dice: GUAU!")

    # Función factory method: Crea una instancia por defecto
    @classmethod
    def factory(cls):
        # Es igaul a return Perro("Chacito Feliz", 4)
        return cls("Chacito Feliz", 4)

    # También se puede hacer un método privado
    def __mi_metodo_privado(self):
        print("¡Este es un método privado!")


# ================================================================================================
perro1 = Perro.factory()
perro1.habla()
# print(perro1.__nombre)  # No se puede acceder desde afuera, imprime error
print(perro1.get_nombre())

# Aunque la propiedad es privada, aún se puede acceder con este método (instancia.__dict__)
print(perro1.__dict__)  # Acceder a al diccionario de las propiedades y su valor

# También se puede acceder de esta forma (intancia._clase__propiedad privada)
print(perro1._Perro__nombre)

perro2 = Perro("Juan", 45)
perro2.habla()
print(perro2.get_nombre())

# Intentar acceder a un método privado (es una convención, no un bloqueo)
# perro1.__mi_metodo_privado()  # Esto podría generar un AttributeError

# Sin embargo, puedes acceder al método privado usando el nombre especial
perro1._Perro__mi_metodo_privado()  # objeto._MiClase__mi_metodo_privado()
