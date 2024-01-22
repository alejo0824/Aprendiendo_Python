animal = "chanchito feliz"
animal2 = "CHANCHO"
animal_con_espacios = "      chancho            "

# upper Convertir todo un string en mayúscula
print(animal.upper())

# lower: Convierte un string en minúscula
print(animal2.lower())

# capitalize: la primera letra en mayúsula
print(animal.capitalize())

# title: La primera letra de cada palabra en mayúscula
print(animal.title())

# strip: Elimina los espacios del inicio y el final
print(animal_con_espacios.strip())

# también esta lstrip para eliminar los espación de la
# izquiers y rstrip para eliminar los espacios de la derecha
print(animal_con_espacios.lstrip())
print(animal_con_espacios.rstrip())

# find: para buscar un carácter en especial. si lo encuentra
# devuelve el número del indice, el primero de izquierda a derecha

# replace: Cambia un caracter por otro
print(animal.replace("nch", "j"))

print("nch" in animal)  # Devuelve True o False si se encuentra
