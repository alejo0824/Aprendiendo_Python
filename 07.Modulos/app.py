""" un módulo es simplemente un archivo que contiene código Python. 
El código en un módulo puede definir funciones, clases y variables, 
y puede ejecutar cualquier código que sea necesario. Los módulos 
son una forma de organizar y reutilizar el código en Python. """

# Importando el módulo del archivo usuario y sus funciones
# from usuario import guardar, pagar_impuesto # DESCOMENTAR

# Importando paquetes
from usuarios.acciones.utilidades import guardar
# NOTA: Varias formas de referenciar paquetes


guardar()
# Los módulos son una herramienta fundamental en Python para organizar
# y estructurar el código, y facilitan la reutilización de código
# en diferentes partes de un proyecto o incluso en proyectos diferentes.

# NOTA: Evitar usar import * ya que pueden haber funciones en nuestro
#       código principal como en el módulo
