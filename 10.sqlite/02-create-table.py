import sqlite3

con = sqlite3.connect("10.sqlite/app.db")
# 1. Crea un objeto **cursor** que actúa como un intermediario para
# ejecutar consultas SQL en la base de datos.
cursor = con.cursor()

# 2. Ejecuta una consulta SQL para crear una tabla llamada usuarios
# si no existe. Esta tabla tendrá dos columnas: id, que es un número
# entero único y clave primaria, y nombre, que es una cadena de
# caracteres de hasta 50 caracteres.
cursor.execute(
    """
  CREATE TABLE IF NOT EXISTS usuarios
  (id INTEGER primary key, nombre varchar(50));
  """
)

# 3. Llama al método commit() en la conexión para confirmar los cambios realizados
# en la base de datos. Esto es importante para que los cambios se guarden
# permanentemente.
con.commit()

# 4. Cerrar la base de datos
con.close()
