mascotas = ["Pelusa", "Pulga", "Felipe", "Wolfgang", "Chanchito Feliz"]

# El método Count Cuenta las veces que puede estar un elemento dentro de una lista.add()
# Si el elemento no está, sale error
print(mascotas.count("Wolfgang"))
if "Wolfgang" in mascotas:  # El if es necesario con index ya que imprime error
    print(mascotas.index("Wolfgang"))
