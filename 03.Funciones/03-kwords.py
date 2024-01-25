"""Esto permite pasar un número variable de argumentos de palabras clave.
Estos argumentos se agrupan en un diccionario, para este caso
un diccionario llamado datos. """


def get_product(**datos):
    print(datos)

    # Si nesecito imprimir un parametro en especifico se usa los <["nombre del argumento"]>
    print(datos["name"], datos["id"])


# Es necesario nombrar el argumento e Imprime un diccionario {dato:"valor"}
get_product(id="50",
            name="iPhone",
            desc="Esto es un Iphone")

# Resultado del diccionario
# {'id': '50', 'name': 'iPhone', 'desc': 'Esto es un Iphone'}
