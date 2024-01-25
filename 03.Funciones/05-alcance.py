# El "alcance" en Python se refiere al ámbito o contexto en el que las variables
# y nombres son accesibles y pueden ser referenciados. Python utiliza reglas de
# alcance para determinar qué variables están disponibles en un lugar específico del código.

# Existen dos tipos principales de alcance en Python:

# ============================== Alcance Local (Local Scope) ==============================

# Las variables definidas dentro de una función tienen un alcance local. Estas variables
# solo son accesibles dentro de la función en la que se definen.

def ejemplo():
    variable_local = 10
    print(variable_local)


ejemplo()  # Esto imprimirá 10

# Esto generará un error, ya que la variable_local no está definida fuera de la función
# print(variable_local) # **Descomentar**

# ============================== Alcance Global (Global Scope): ==============================

# Las variables definidas fuera de cualquier función o bloque de código tienen un alcance
# global. Estas variables son accesibles desde cualquier lugar en el script o módulo

# NOTA: Las variables globales son malas practicas

variable_global = 20


def ejemplo2():
    print(variable_global)


ejemplo2()  # Esto imprimirá 20
print(variable_global)  # Esto imprimirá 20 también
