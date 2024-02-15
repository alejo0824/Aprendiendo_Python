from pathlib import Path

# Define la ruta del archivo llamado "archivo-prueba.txt" en una ubicación específica dentro de
# la estructura de archivos.
archivo = Path("09.archivos/archivo-prueba.txt")

# Lee el contenido del archivo como texto utilizando el método read_text()
# de la clase Path, utilizando el formato de codificación UTF-8. Luego,
# divide el texto en líneas individuales mediante split("\n"), lo que crea
# una lista de líneas de texto.
text = archivo.read_text("utf-8").split("\n")
# Inserta la cadena "Hola Mundo" al principio de la lista de líneas de texto utilizando
# el método insert() de las listas.
# Insertar Hola Mundo - Modificamos el archivo original
text.insert(0, "Hola Mundo - Modificamos el archivo original")

# Finalmente, escribe el texto resultante de nuevo en el archivo, sobrescribiendo
# su contenido anterior, utilizando el método write_text() de la clase Path,
# nuevamente especificando UTF-8 como formato de codificación.
archivo.write_text("\n".join(text), "utf-8")

# Desafíos: Sobreescribir un archivo muy grande de esta manera puede no ser eficiente ni recomendable.
