""" En este caso, como se utiliza la estructura with, no es necesario llamar 
explícitamente a los métodos commit() y close() en la conexión a la base de 
datos. La estructura with se encarga de manejar esto automáticamente, 
asegurando que los cambios se guarden y la conexión se cierre correctamente
al salir del bloque. """

import sqlite3

# Con with no es necesario los métodos close y commit,
# ya que with trae el método magico __exit__ que a su vez trae el commit y el close
with sqlite3.connect("10.sqlite/app.db") as con:

    # 1. Crea un objeto **cursor** que actúa como un intermediario para
    # ejecutar consultas SQL en la base de datos.
    cursor = con.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS usuarios
    (id INTEGER primary key, nombre varchar(50));
    """
    )
