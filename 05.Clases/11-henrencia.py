""" La herencia es un concepto fundamental en la programación orientada a objetos (OOP)
que permite la creación de nuevas clases que heredan atributos y métodos de clases 
existentes. En Python, la herencia se implementa de la siguiente manera: """


class ClaseBase:
    def __init__(self, atributo_base):
        self.atributo_base = atributo_base

    def metodo_base(self):
        print("Método de la clase base")


class ClaseDerivada(ClaseBase):
    def __init__(self, atributo_base, atributo_derivado):
        # Llamar al constructor de la clase base
        super().__init__(atributo_base)
        self.atributo_derivado = atributo_derivado

    def metodo_derivado(self):
        print("Método de la clase derivada")


# Crear una instancia de la clase derivada
objeto_derivado = ClaseDerivada("Base", "Derivado")

# Acceder a los atributos y métodos de ambas clases
print(objeto_derivado.atributo_base)  # Imprime "Base"
objeto_derivado.metodo_base()         # Imprime "Método de la clase base"
print(objeto_derivado.atributo_derivado)  # Imprime "Derivado"
# Imprime "Método de la clase derivada"
objeto_derivado.metodo_derivado()
