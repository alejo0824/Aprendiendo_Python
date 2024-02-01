""" El método constructor en Python es un método especial llamado __init__ que se utiliza
para inicializar los atributos de una instancia de una clase cuando se crea.
Esencialmente, el método constructor define cómo se debe construir (inicializar)
un objeto cuando se instancia la clase.

El método __init__ se llama automáticamente cuando se crea una nueva instancia de la clase.
La palabra clave self en el método se refiere a la instancia recién creada,
y se utiliza para asignar valores a los atributos de esa instancia. """


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):  # Esto se convierte en métodos y el primer parámetro es Self
        print(f"{self.nombre} Dice: GUAU!")

# La palabra clave <self> se refiere a la instancia de la clase y se utiliza para
# acceder a los atributos y métodos de esa instancia dentro de los métodos de la clase.


# Crear una instancia de la clase Perro y llamar al método habla
mi_perro = Perro("Chanchito", 25)
mi_perro.habla()  # Imprime "Chanchito Dice: GUAU!"
