""" <@classmethod> es un decorador que se utiliza para definir un método
de clase en una clase. Un método de clase es un método que se asocia
con la clase en lugar de con las instancias individuales de la clase.
El primer parámetro de un método de clase es la propia clase,
por convención denominado cls (aunque puedes usar cualquier nombre). """

# Aquí hay un ejemplo de cómo se utiliza @classmethod:


class Perro:

    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod  # Toma el método global de la clase
    def habla(cls):  # cambia el self por cls
        print("GUAU!")

    # Función factory method: Crea una instancia por defecto
    @classmethod
    def factory(cls):
        # Es igaul a return Perro("Chacito Feliz", 4)
        return cls("Chacito Feliz", 4)


Perro.habla()
Perro1 = Perro("Chanchito", 2)
Perro2 = Perro("Felipe", 3)
Perro3 = Perro.factory()
print(Perro3.nombre, Perro3.edad)
print(Perro2.nombre, Perro2.edad)

# Los métodos de clase son útiles cuando necesitas realizar operaciones que
# están relacionadas con la clase en lugar de con instancias específicas.
# Pueden ser utilizados para realizar tareas que involucran la clase en
# sí misma o para crear instancias específicas de la clase.

# EJEMPLO 2


class MiClase:
    propiedad_compartida = "Valor compartido"

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

    @classmethod
    def metodo_de_clase(cls, parametro_clase):
        print(f"Método de clase llamado con {cls} y {parametro_clase}")


# Crear una instancia de la clase
objeto1 = MiClase("Instancia 1")

# Llamar al método de clase desde la clase
MiClase.metodo_de_clase("parámetro_1")
# Imprime "Método de clase llamado con <class '__main__.MiClase'> y parámetro_1"

# Llamar al método de clase desde una instancia
objeto1.metodo_de_clase("parámetro")
# Imprime "Método de clase llamado con <class '__main__.MiClase'> y parámetro"
