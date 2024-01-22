nombre_curso = "Ultimate Pyhon"  # Se definen con doble comillas
nombre_cuso2 = 'Ultimate Python'  # También de comillas sencilla

nombre_muy_grande = """
Para escribir un texto muy graden usamos las 
tripes comillas 
"""

# ==========================================Funciones==========================================
# Devuelve el valo de la cantidad de caracteres del argumento
print(len(nombre_curso))

# También podemos extraer algún carácter en especifico,en este caso el primero
print(nombre_curso[0])

# También podemos traer una porción de una cadena de texto.ya que toma los caracteres
# desde el índice 0 hasta el índice 7 (8 no incluido).
print(nombre_curso[0:8])

# en este caso, extraerá una porción de la cadena a partir del noveno carácter
# hasta el final de la cadena.
print(nombre_curso[9:])

# En este caso, extraerá una porción de la cadena desde el inicio hasta
# el octavo carácter (el índice 8 no incluido)
print(nombre_curso[:8])
