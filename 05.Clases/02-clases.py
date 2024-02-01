# ========================================= Creando una clase en Python=========================================
# Se usa la palabra clave <class> se utiliza para definir una clase llamada

class Perro:
    # Las funciones de una clase se llaman MÉTODOS, que son funciones de una clase
    # <self> es una convención utilizada como el primer parámetro de los métodos de una clase.
    def ladra(self):
        print("Guau!")


# Crear una instancia de la clase Perro
mi_perro = Perro()

# Establecer un ladrido de mi instancia Mi perro utilizando un método
mi_perro.ladra()

# Saber si la instancia mi_perro pertenece a la clase Perro
# (True o False)
print(isinstance(mi_perro, str))
