import random
import string

lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)  # Mezcla aleatoriamente los elementos de la lista lista
print(
    random.random(),  # Imprime un número aleatorio entre 0 y 1.
    # Imprime un número entero aleatorio en el rango de 1 a 10.
    random.randint(1, 10),
    # Imprime la lista lista después de haber sido mezclada aleatoriamente.
    lista,
    # Imprime un elemento aleatorio de la lista lista2.
    random.choice(lista2),
    # : Imprime una lista de 3 elementos seleccionados aleatoriamente de la lista lista2,
    # permitiendo selecciones repetidas.
    random.choices(lista2, k=3),
    # Imprime una lista de 3 caracteres aleatorios
    random.choices("abcdefghij,123", k=3),
)

# Crea una cadena que contiene todas las letras ASCII, tanto mayúsculas como minúsculas.
chars = string.ascii_letters
# Crea una cadena que contiene los dígitos del 0 al 9.
digitos = string.digits

# Crea una lista de 16 caracteres seleccionados aleatoriamente de la combinación de
# letras y dígitos.
seleccion = random.choices(chars + digitos, k=16)
print(seleccion)

# Une los caracteres seleccionados aleatoriamente en una cadena para formar una contraseña.
contrasena = "".join(seleccion)
print(contrasena)
