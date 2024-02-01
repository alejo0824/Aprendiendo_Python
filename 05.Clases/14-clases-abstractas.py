""" Una clase abstracta es una clase que no puede ser instanciada
directamente y que generalmente contiene uno o más métodos abstractos.
<<Un método abstracto es un método>> que está declarado en la clase
abstracta pero no proporciona una implementación. En lugar de eso, las
clases que heredan de la clase abstracta deben proporcionar una 
implementación concreta para los métodos abstractos.

Para crear una clase abstracta en Python, puedes utilizar el 
módulo <<abc (Abstract Base Classes)>> que proporciona la capacidad 
de definir clases y métodos abstractos. Aquí hay un ejemplo básico: """

# PARA CLASES QUE NO ESTÁ DISEÑANADA PARA GENERAR INSTANCIAS

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio**2

    def calcular_perimetro(self):
        return 2 * 3.14 * self.radio

# Intentar instanciar la clase abstracta generará un error
# figura = FiguraGeometrica()  # Generará un TypeError


# Crear una instancia de la subclase
circulo = Circulo(5)

# Llamar a los métodos de la subclase
print("Área del círculo:", circulo.calcular_area())
print("Perímetro del círculo:", circulo.calcular_perimetro())


# • FiguraGeometrica es una clase abstracta que define dos métodos abstractos:
#   calcular_area y calcular_perimetro. (NO SE PUEDE INSTANCIAR)
# • Circulo es una subclase de FiguraGeometrica y proporciona implementaciones
#   concretas para los métodos abstractos.

# Si intentas instanciar directamente la clase abstracta (FiguraGeometrica),
# Python generará un error TypeError. La idea es que las clases abstractas
# sirvan como interfaces que otras clases deben implementar.

# La creación de clases abstractas y métodos abstractos permite definir interfaces
# comunes para un conjunto de clases relacionadas, garantizando que todas las
# clases que heredan de la clase abstracta implementen ciertos métodos específicos.
# Esto puede ser útil para establecer un contrato común en el diseño de clases en
# situaciones donde las clases comparten ciertas funcionalidades pero pueden
# tener implementaciones específicas.
