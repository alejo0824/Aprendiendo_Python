# Almacenar Objetos dentro de Objetos

class Producto:
    def __init__(self, nombre, precio) -> None:
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos) -> None:
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


# Definiendo instancias de productos para deporte
kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboar = Producto("Surfboar", 500)

# Definiendo instancia de la categoría "Deportes" y almacenados instancias
# del objeto producto
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.agregar(surfboar)
deportes.imprimir()
