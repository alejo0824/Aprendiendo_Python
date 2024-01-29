mascotas = [
    "Wolfgang",
    "Pelusa",
    "Pulga",
    "Felipe",
    "Pulga",
    "Chanchito Feliz"
]

# Agregar elemento en un índice especidfico
mascotas.insert(1, "Melvin")  # Indice, valor

# Agregar al final un elementeo
mascotas.append("Chanchito Triste")

# Eliminar el elemento que queremos eliminar
mascotas.remove("Pulga")  # Elimina la primera ocurrencia

# Eliminar el último elementeo
mascotas.pop()  # Dentro de POP se puede colocar el índice a eliminar

# también se puede eliminar de esta forma el valor desde el índice
del mascotas[0]

mascotas.clear()  # Borro todos los elementos
print(mascotas)
