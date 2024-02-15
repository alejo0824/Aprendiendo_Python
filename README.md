# Aprendiendo Python 

## Introducción 

- El REPL, que significa **"Read Eval Print Loop" (Lectura, Evaluación, Impresión y Bucle)**, es un intérprete interactivo de Python. Puedes ejecutarlo directamente desde la consola utilizando el comando "python" o "python3" en sistemas operativos Linux y macOS. Este entorno te permite ingresar instrucciones de Python línea por línea, evaluándolas inmediatamente y mostrando los resultados. Es una herramienta valiosa para explorar y experimentar con el lenguaje de programación Python de manera interactiva, facilitando el aprendizaje y la experimentación directa con el código.

- Usamos formateador autopep8: es una herramienta en Python que se utiliza para formatear automáticamente el código fuente según las convenciones de estilo definidas en PEP 8 (Propuesta de Mejora de Python número 8). PEP 8 es el documento que describe las recomendaciones y directrices para escribir código Python legible y consistente.

- ### Extensiones para Visula Studio Code
  + **Python de Migrosoft:** proporciona un entorno integrado y eficiente para el desarrollo de aplicaciones en Python, ofreciendo características como resaltado de sintaxis, sugerencias de código, depuración y gestión de entornos virtuales.
  + **Pylint:** proporciona una herramienta de análisis estático para Python, ayudando a detectar y corregir posibles problemas en el código mediante la identificación de errores, estilo y prácticas recomendadas.
  
-------------
## 01 Tipos de Datos 
- ### Variables tipo String
    * Definición de variables de tipo String
    * Métodos para variables de tipo String
    * Manipulación de variables tipo String
- ### Variables Tipo Númerica
    * Definición de variables de tipo númericos
    * Métodos para variables de tipo númericos
    * Módulo Math 
    * Calculadora simple 
-------------
## 02 Control de flujo 
- ### If, if - else, if - elif - else
    + Estrutura básica de los condicionales If, if - else, if - elif - else
    + operador ternarío.
    + Cadena de operadores 
- ### Ciclos
    + #### Ciclo For
      + For 
      + For else
    + #### Cliclo While
-------------
## 03 Funciones 
  Una función es un bloque de código reutilizable que realiza una tarea específica. Las funciones permiten organizar el código de manera modular, lo que facilita la comprensión y el mantenimiento del programa. Una función en Python se define utilizando la palabra clave def, seguida del nombre de la función y paréntesis que pueden contener los parámetros de entrada.Aquí tienes un ejemplo simple de una función en Python:

  ```py
  def saludar(nombre):
    """
    Esta función imprime un saludo personalizado.
    """
    print(f"Hola, {nombre}!")

    # Llamada a la función
    saludar("Alejandro")
  ```

  Los temas a tratar fueron:

  +  #### Introducción a funciones 
      - Parámetros y argumentos
      - Argumentos Opcionales 
      - Argumentos nombrados
      
  + **X args**: recibir un número indeterminado de argumentos
  +  **k-words** : Agrupar valores en un diccionario
  + **Return**: Para devolver el valor de una función
  + **Alcance**: el Scope en Python
  + **Depuración** Como depurar en VSC
---

## 04 Tipos de datos 
Los tipos de datos en programación se refieren a las categorías o clases de datos que pueden ser utilizadas y manipuladas en un programa. Los tipos de datos definen las características y operaciones que se pueden realizar con los datos. Los lenguajes de programación, incluyendo Python, tienen varios tipos de datos incorporados que se utilizan para representar diferentes tipos de información.

  - ### Listas
    + Definición y usos de las listas 
    + Manipulación de listas
    + Desempaquetar Listas 
    + Las formas más comunes de iterar una lista
    + Ordenar listas con la función sort
    + listas de compresión

  - ### Tuplas
  - ### Sets
  - ### Diccionarios
  - ### Desempaquetamiento 
  - ### Filas y Pilas
---  
## 05 Clases 
  - ### Creación de una clase 
  - ### Método Constructor 
  - ### Propiedades "privadas" 
  - ### Uso del @classmethod
  - ### Decorador Property y Setter (Forma más sencilla del acceder a una propiedad)
  - ### Métodos Mágicos
    + **Comparación de objetos**
  - ### Contenedores: Objetos dentro de otros objetos
  - ### Herencia
    + **Herencia múltiple**
    + **Anulación de Método**
    + **Extendiendo tipos nativos de Python** (clase 17)
  - ### Clases abstractas 
  - ### Polimorfismo 
    + **Duck Typing**
---  
## 06 Excepciones
  + Tipos de excepciones
  + Uso del bloque Else y Finally 
  + Lanzar excepciones en el código 
  + Excepciones personalizadas 
---  
## 07 Módulos
  + Importando un módulo (usuario) a nuesto código principal(app)
  + **Archivo \_\_pycache\_\_**: Se genera por Python para almacenar archivos de código fuente compilados en formato de bytecode específico de la versión de Python que está utilizando. Esto se hace para mejorar el rendimiento al evitar la necesidad de recompilar el código fuente cada vez que se ejecuta el programa. **Es para mejorar el rendimiento de carga de módulos**
  + Paquetes 
    + Subpaquetes
---  
## 08 Manejo de Rutas y Directorios 
  + Métodos, propiedades y usos con pathlib 
  + Manejo de Directorios (Se crean las carpetas "uno" y "dos" para esta demostración). Asegúrate de estar en la terminal en la raíz antes de ejecutar el código.
  + Inyección de depencias con pathlib
---

## 09 Manejo de Archivos
 + Uso de la fución **ctime** de la kibrería **time** para ver la fecha y hora de la última modificación de un archivo en un formato legible 
 + Lectura y escritura con el archivo "archivo-prueba.txt" a través del la librería **Path** y **Open** 
 + Manejo de archivos **CSV**: Lectura y escritura 
 + Manejo de archivos **JSON**: Lectura y escritura
 + Manejo de archivos **Comprimidos**: Lectura y escritura
 + Comprimir y Descomprimir Archivos **ZIP** (No se suben al repositorio los ZIP)