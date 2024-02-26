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
 ---
 ## 10 SQL 
 Para está sección utilizaremos una sqlite3 como ejemplo ya que se  usa para manejar bases de datos pequeña
 + Creación de una base de datos
 + Formas de hacer una consulta con Python (con **open-commit** y **with**)
 + Leer información en una base de datos
 --- 
 ## 11 Módulos Nativos 
 Son bibliotecas de Python que vienen preinstaladas con la distribución estándar de Python. Estas bibliotecas proporcionan una amplia gama de funcionalidades que van desde operaciones básicas de manipulación de datos hasta la interacción con sistemas operativos, manejo de archivos, acceso a bases de datos, manipulación de cadenas, procesamiento de archivos y mucho más.
  + **Web Browser:** Proporciona funciones para abrir páginas web en un navegador web predeterminado
  + **Manejo de Fechas, horas y tiempos :** Desde el módulo nativo datetime y sus paquetes datetime, timedelta
  + **Random:**  proporciona funciones para trabajar con la generación de números aleatorios y operaciones relacionadas con la aleatoriedad
  + **Cli:** Aplicaciones para la línea de comandos. *Se debe ejecutar desde consola y dentro de la carpeta* 
  + **Envio de Correos** 
---

## 12 Módulos
  + ### PyPI
    es el Índice de Paquetes de Python (Python Package Index, en inglés), un repositorio en línea de software desarrollado y mantenido por la comunidad de Python. PyPI contiene paquetes de software de Python de código abierto que pueden ser instalados utilizando la herramienta pip (pip instala paquetes de Python) que viene incluida con Python desde la versión 3.4 en adelante. Los paquetes alojados en PyPI abarcan una amplia gama de funcionalidades y propósitos, desde herramientas de desarrollo hasta aplicaciones completas, y son una parte esencial del ecosistema de desarrollo de Python.

      + **Instalción** Para encontrar un índice de paquetes de Python, puedes buscar en este [Enlace](https://pypi.org/). Por ejemplo, para instalar Django, puedes encontrarlo allí.

        #### Cómo instalar un paquete usando pip en Python

        1. Abre una terminal o línea de comandos en tu sistema operativo.
          
        2. Utiliza el comando `pip install` seguido del nombre del paquete que deseas instalar. Por ejemplo, para instalar el paquete `requests`, puedes escribir:

            ```
            pip install requests
            ```

        3. Presiona Enter y pip comenzará a descargar e instalar el paquete y sus dependencias automáticamente.

        4. Una vez completada la instalación, puedes comenzar a utilizar el paquete en tu código de Python importándolo como cualquier otro módulo. Por ejemplo:

            ```python
            import requests
            ```

        Eso es todo. Ahora tienes el paquete instalado y listo para ser utilizado en tus proyectos de Python.

  + ### Crear un ambiente virtual en Python
  
    #### 1. Instalación de virtualenv

    Si aún no tienes instalado `virtualenv`, puedes hacerlo utilizando `pip`, el gestor de paquetes de Python. Abre tu terminal y ejecuta el siguiente comando:

    ```bash
    pip install virtualenv
    ```  
    #### 2. Crear el Ambiente Virtual

    Una vez instalado `virtualenv`, decide dónde deseas crear tu proyecto y navega a ese directorio en tu terminal. Luego, ejecuta el siguiente comando para crear un nuevo ambiente virtual. Puedes reemplazar `nombre_del_ambiente_virtual` con el nombre que desees darle a tu ambiente virtual:

    ```bash
    virtualenv nombre_del_ambiente_virtual
    ```

    #### 3. Activar el Ambiente Virtual

    Dependiendo de tu sistema operativo, el comando para activar el ambiente virtual variará:

    - **En sistemas basados en Unix/Linux/macOS**:

      ```bash
      source nombre_del_ambiente_virtual/bin/activate
      ```
    - **En sistemas basados en Windows**:

      ```bash      
      nombre_del_ambiente_virtual\Scripts\activate
      ```
    Una vez ejecutado el comando correspondiente, estarás dentro de tu ambiente virtual y podrás empezar a trabajar en tu proyecto.
    #### 4. Listo

    Ahora estás dentro de tu ambiente virtual. Puedes instalar paquetes específicos de Python y trabajar en tu proyecto sin afectar el entorno global de Python en tu sistema. Cuando termines de trabajar, puedes desactivar el ambiente virtual ejecutando el comando `deactivate`.


  + ### Pipenv: Gestión Moderna de Entornos y Dependencias en Python

    "Pipenv" es una herramienta de gestión de entornos y dependencias de Python que proporciona una forma más moderna y simplificada de manejar estos aspectos en comparación con herramientas más antiguas como "virtualenv" y "pip".

      #### Características y Ventajas de Pipenv:

      1. **Gestión de Dependencias Simplificada**:
        - Combina las funcionalidades de "pip" y "virtualenv" en una sola herramienta, facilitando la gestión de dependencias.

      2. **Gestión Automática de Entornos Virtuales**:
        - Al iniciar un nuevo proyecto o instalar nuevas dependencias, Pipenv automáticamente crea y gestiona un entorno virtual para el proyecto, eliminando la necesidad de crearlos manualmente.

      3. **Resolución Precisa de Dependencias**:
        - Utiliza "Pipfile" y "Pipfile.lock" para gestionar las dependencias y sus versiones de forma precisa, garantizando la instalación consistente de dependencias en diferentes entornos.

      4. **Activación Sencilla del Entorno Virtual**:
        - Proporciona un comando sencillo (`pipenv shell`) para activar el entorno virtual del proyecto, facilitando el trabajo dentro del entorno virtual.

      En resumen, Pipenv es una herramienta popular y potente para gestionar entornos y dependencias de proyectos de Python. Es especialmente útil para simplificar el flujo de trabajo de desarrollo y garantizar la consistencia en la gestión de dependencias en diferentes entornos.
---
## 13 Paquetes Populares
### Configuración de variables de entorno 
Las variables de entorno en Python son configuraciones a nivel del sistema operativo que proporcionan información específica que los programas pueden utilizar durante su ejecución, accesibles a través del módulo os utilizando os.environ['NOMBRE_VARIABLE']. 

**NOTA: Se crea el archivo .env para las variables de entorno pero no se sube al repositorio. También se crea un ambiente virtual con pipenv y estar dentro de la carpeta '13.Paquetes-Populares'**

  - #### Sendgrid
    SendGrid es una plataforma en la nube que permite a empresas enviar correos electrónicos de manera confiable y escalable. Ofrece una API fácil de usar, análisis detallados y plantillas personalizables para facilitar el envío y seguimiento de correos electrónicos transaccionales y de marketing.
  - #### SMS con Twilio
    Twilio es una plataforma de comunicaciones en la nube que permite a los desarrolladores integrar fácilmente funcionalidades de mensajería y voz en sus aplicaciones utilizando APIs simples y potentes. Algunos de los servicios que ofrece 

  - #### API REST con la librería Requests
    Una API REST (*Representational State Transfer*) es un conjunto de principios de diseño arquitectónico que se utiliza para crear servicios web que sean escalables, flexibles y fáciles de mantener. Este enfoque se basa en el concepto de recursos, los cuales son identificados mediante URLs (Uniform Resource Locators), y la interacción con estos recursos a través de métodos HTTP estándar, como GET, POST, PUT, DELETE, entre otros.

    Aquí hay algunas características clave de una API REST:

    1. **Basada en recursos**: En una API REST, los recursos (como usuarios, productos, publicaciones de blog, etc.) son el centro de atención. Cada recurso se identifica mediante una URL única, y la manipulación de estos recursos se realiza a través de las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) utilizando métodos HTTP.

    2. **Sin estado (stateless)**: Las solicitudes a una API REST no mantienen estado entre ellas. Cada solicitud contiene toda la información necesaria para procesarla, lo que hace que las APIs REST sean altamente escalables y fáciles de gestionar.

    3. **Interfaz uniforme**: Las APIs REST utilizan un conjunto uniforme de operaciones estándar de HTTP, como GET para obtener datos, POST para crear nuevos recursos, PUT para actualizar recursos existentes y DELETE para eliminar recursos.

    4. **Formato de datos flexible**: Los datos intercambiados entre el cliente y el servidor pueden estar en varios formatos, como JSON (JavaScript Object Notation) o XML (eXtensible Markup Language), aunque JSON es más comúnmente utilizado debido a su simplicidad y ligereza.

    5. **Independencia de la capa de transporte**: Las APIs REST pueden utilizar cualquier protocolo de transporte, pero son más comúnmente implementadas sobre HTTP debido a su amplia disponibilidad y facilidad de uso.

    En resumen, una API REST proporciona una forma estandarizada y flexible de intercambiar datos entre sistemas distribuidos a través de la web, utilizando los principios de la arquitectura REST. Esto permite una integración eficiente entre aplicaciones y servicios, lo que es fundamental en el desarrollo de aplicaciones modernas y escalables.
- #### El web scraping con BeautifulSoup4
  Es la práctica de automatizar la extracción de datos de páginas web. Utiliza programas para recorrer sitios web y extraer información como texto, imágenes o enlaces. Se utiliza para diversos fines, como análisis de datos, seguimiento de precios o monitoreo de la competencia. Es importante tener en cuenta las consideraciones legales y éticas al realizar web scraping, ya que puede haber restricciones por parte de los sitios web en cuanto a la recopilación de sus datos.

    
  Con BeautifulSoup4, una popular biblioteca de Python para analizar y extraer datos de HTML y XML, el proceso de web scraping se simplifica

- #### Excel con openpyxl
  **openpyxl** es una biblioteca de Python que permite trabajar con archivos de Excel (.xlsx). Permite crear nuevos archivos de Excel, leer datos de archivos existentes, modificar archivos de Excel y escribir datos en ellos.

  Algunas de las funcionalidades principales de **openpyxl** incluyen:

  1. **Crear archivos de Excel**: Permite crear nuevos archivos de Excel desde cero, con hojas de cálculo y celdas personalizadas.

  2. **Leer datos de archivos de Excel**: Permite leer datos de archivos de Excel existentes, incluidos valores de celdas, formatos, fórmulas y más.

  3. **Modificar archivos de Excel**: Permite modificar archivos de Excel existentes, como cambiar valores de celdas, agregar o eliminar hojas de cálculo, aplicar estilos y formatos, y más.

  4. **Escribir datos en archivos de Excel**: Permite escribir datos en archivos de Excel, como valores de celdas, fórmulas, estilos y más.

  **openpyxl** es una biblioteca poderosa y ampliamente utilizada para manipular archivos de Excel en Python. Es particularmente útil para tareas como análisis de datos, generación de informes, automatización de tareas de oficina y más.
