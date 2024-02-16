import sqlite3

with sqlite3.connect("10.sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        # La consulta utiliza un marcador de posición ? para prevenir la inyección de SQL.
        " INSERT INTO usuarios values(?,?)",
        (1, "Hola Mundo"),

    )

# En resumen, este código inserta un nuevo registro en la tabla usuarios con el valor 1 en la
# columna id y el valor "Hola Mundo" en la columna nombre. Además, al utilizar la estructura
# with, se garantiza que la conexión se cierre correctamente al salir del bloque,
# sin necesidad de llamar explícitamente al método commit() o close().
