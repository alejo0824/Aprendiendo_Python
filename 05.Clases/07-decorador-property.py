""" una propiedad de solo lectura. Proporciona una forma de definir un 
método que puede ser accedido como si fuera un atributo, sin la 
necesidad de invocar el método con paréntesis. Esto puede ser útil 
cuando quieres encapsular la lógica de acceso a un atributo y proporcionar una 
interfaz más limpia para obtener su valor. """


class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    # Forma más elegante de leer el nombre
    @property  # Para funciones que queremos retornar (get_nombre)
    def nombre(self):
        print("Pasando por getter")
        return self.__nombre

    # Este método funciona como un setter y se encarga de imprimir "Pasando por el setter"
    @nombre.setter  # También definir el setter
    def nombre(self, nombre):
        print("Pasando por el setter")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("Choclo")
print(perro.nombre)

perro.nombre = "Juan"  # Ya se puede modificar el nombre
print(perro.__dict__)

print(perro._Perro__nombre)
