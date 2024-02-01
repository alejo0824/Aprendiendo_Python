""" puedes extender o modificar el comportamiento de tipos nativos mediante
la herencia o mediante el uso de la composición. Aquí te hay un ejemplo
utilizando herencia para extender una lista: """


class ListaPersonalizada(list):
    def suma_elementos(self):
        return sum(self)


# Crear una instancia de la ListaPersonalizada
mi_lista = ListaPersonalizada([1, 2, 3, 4, 5])

# Utilizar métodos de la lista extendida
# Imprime: Lista extendida: [1, 2, 3, 4, 5]
print("Lista extendida:", mi_lista)
# Imprime: Suma de elementos: 15
print("Suma de elementos:", mi_lista.suma_elementos())

# En este ejemplo, hemos creado una nueva clase llamada <<ListaPersonalizada>>
# que hereda de la clase nativa list. Luego, hemos añadido un método adicional
# llamado suma_elementos. Cuando creamos una instancia de ListaPersonalizada,
# podemos utilizar tanto los métodos de la
# clase list como los métodos personalizados que hemos añadido.

# Recuerda que la herencia no es la única manera de extender tipos nativos en
# Python; también puedes usar composición o incluso técnicas de
# monkey patching (modificación en tiempo de ejecución). La elección depende
# de tus necesidades específicas y de las mejores prácticas de diseño de código.
