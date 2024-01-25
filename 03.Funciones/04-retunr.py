"""a palabra clave return se utiliza dentro de una función para 
devolver un valor desde la función. Cuando una función alcanza una 
declaración return, se detiene la ejecución de la función y el valor
especificado después de return se devuelve al punto donde se llamó la 
función. La presencia de un return también puede indicar la finalización 
de la ejecución de la función, incluso si no hay un valor específico para devolver."""


def suma(a, b):
    resultado = a + b
    return resultado


# Llamada a la función y asignación del resultado a una variable
resultado_suma = suma(3, 4)

# Imprime el resultado
print(resultado_suma)  # Imprimirá 7

# Es importante tener en cuenta que una función puede tener múltiples declaraciones return
# (condicionales) o incluso ninguna. Si no hay una declaración return o si la función alcanza el final
# sin una, la función devuelve None de manera implícita.
