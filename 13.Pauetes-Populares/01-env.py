""" ============================== VARIABLES DE ENTORNO ==============================
Las variables de entorno en Python son variables que se configuran a nivel del 
sistema operativo y están disponibles para todos los programas y procesos que se 
ejecutan en ese sistema. Estas variables proporcionan información o configuración e
specífica que los programas pueden utilizar durante su ejecución.

En Python, puedes acceder a las variables de entorno utilizando el módulo os de la 
biblioteca estándar. Por ejemplo, puedes obtener el valor de una variable de 
entorno específica utilizando os.environ['NOMBRE_VARIABLE']. Aquí, 'NOMBRE_VARIABLE' 
es el nombre de la variable de entorno que deseas consultar.

Las variables de entorno se utilizan comúnmente para configurar información como 
rutas de directorio, ajustes de configuración específicos del usuario, claves de 
API y cualquier otra información que pueda ser necesaria para que un programa 
funcione correctamente en un entorno específico.

Las variables de entorno son útiles porque permiten separar la configuración del 
código, lo que hace que los programas sean más portátiles y fáciles de configurar 
en diferentes entornos. Además, proporcionan una forma de compartir información 
de configuración entre diferentes programas o scripts en un sistema. """

import os

# Obtener el valor de la variable de entorno API
apikey = os.environ.get('MI_LLAVE')

# Imprimir el valor de la variable API
print("El valor de la variable API es:", apikey)
