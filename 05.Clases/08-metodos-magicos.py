# son métodos con nombres que tienen doble guion bajo al principio y al final, como __init__ o __str__.
# Estos métodos proporcionan una forma de definir el comportamiento especial de las clases y objetos
# en Python. Cuando ciertas operaciones específicas ocurren en instancias de una clase, Python
# busca y llama automáticamente estos métodos mágicos si están definidos.

# Link para ver métodos mágicos https://rszalski.github.io/magicmethods/#representations

class Perro:

    # Ejecutados indirectamente como __init__
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método mágico destructor
    def __del__(self):
        print(f"Chao perro 😞 {self.nombre}")

    # Permite definir una representación en cadena (string) legible de un objeto
    def __str__(self):
        return f"Clase Perro {self.nombre}"

    def habla(self):
        print(f"{self.nombre} Dice: GUAU!")


perro = Perro("chanchito", 7)
print(perro)

# Imprimir la representación en cadena utilizando str()
texto = str(perro)  # Imprime "Clase Perro chanchito"

print(texto)
# Eliminar todas las referencias al objeto
del perro  # Esto llamará automáticamente a __del__

# En este punto, el recolector de basura puede liberar la memoria de la instancia
