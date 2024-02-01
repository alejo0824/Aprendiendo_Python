""" Las propiedades de clase (también llamadas variables de clase) son atributos
que son compartidos por todas las instancias de una clase en Python. A diferencia
de los atributos de instancia, que son específicos de cada objeto creado a partir
de la clase, las propiedades de clase son comunes a todas las instancias y pertenecen
a la clase en sí. """

# Puedes definir propiedades de clase directamente dentro de la clase y acceder a ellas
# a través de la propia clase o de cualquier instancia de la clase. Aquí hay un ejemplo:


class MiClase:
    # Propiedad de clase
    propiedad_compartida = "Valor compartido"

    def __init__(self, atributo_instancia):
        # Atributo de instancia
        self.atributo_instancia = atributo_instancia


# Crear instancias de la clase
objeto1 = MiClase("Instancia 1")
objeto2 = MiClase("Instancia 2")

# Acceder a la propiedad de clase desde la clase
print(MiClase.propiedad_compartida)  # Imprime "Valor compartido"

# Acceder a la propiedad de clase desde una instancia
print(objeto1.propiedad_compartida)  # Imprime "Valor compartido"
print(objeto2.propiedad_compartida)  # Imprime "Valor compartido"

# Acceder a un atributo de instancia
print(objeto1.atributo_instancia)    # Imprime "Instancia 1"
print(objeto2.atributo_instancia)    # Imprime "Instancia 2"

# Puedo cambiar la propiedad en la Instancia y no en el Objeto
objeto1.propiedad_compartida = "Cambiado"
# Imprime "Cambiado" en vez de "Valor Compartido"
print(objeto1.propiedad_compartida)
