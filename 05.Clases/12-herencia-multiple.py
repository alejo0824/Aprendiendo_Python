""" permite que una clase herede atributos y métodos de más de una clase base. 
Esto se logra listando las clases base separadas por comas en la declaración 
de la clase derivada. La herencia múltiple ofrece flexibilidad al permitir que una 
clase adquiera funcionalidades de varias clases diferentes
 """


class ClaseA:
    def metodo_a(self):
        print("Método de ClaseA")

    def metodo_comun(self):
        print("Método común de ClaseA")


class ClaseB:
    def metodo_b(self):
        print("Método de ClaseB")

    def metodo_comun(self):
        print("Método común de ClaseB")


class ClaseC(ClaseA, ClaseB):
    def metodo_c(self):
        print("Método de ClaseC")


# Crear una instancia de la clase derivada ClaseC
objeto_c = ClaseC()

# Acceder a los métodos de las clases base
objeto_c.metodo_a()  # Imprime "Método de ClaseA"
objeto_c.metodo_b()  # Imprime "Método de ClaseB"
objeto_c.metodo_c()  # Imprime "Método de ClaseC"

# NOTA: Utilizará el método de la primera clase base mencionada en la lista
# de herencia. Esto se conoce como la regla del "orden de resolución de métodos"
# en otras palabara, llamará al método de la primera clase invocada. En este caso ClaseA
#  porque fue invocada primero
objeto_c.metodo_comun()
