# Python_Entornos_Virtuales
# Cómo crear el entorno virtual

Para crear el entorno virtual se utilizó la herramienta venv incluida en Python. Primero se abrió la terminal dentro de la carpeta del proyecto y se ejecutó el siguiente comando:

python -m venv venv

Este comando creó una carpeta llamada “venv” que contiene todos los archivos necesarios del entorno virtual. Posteriormente, el entorno se activó utilizando:

venv\Scripts\activate

Al activarse correctamente, la terminal muestra el nombre del entorno virtual al inicio de la línea de comandos. El uso de entornos virtuales permite trabajar con dependencias aisladas y evitar conflictos entre diferentes proyectos de Python.

# Cómo instalar dependencias

Para instalar las dependencias necesarias del proyecto se utilizó pip, el gestor de paquetes de Python. En este caso se instaló la librería python-dotenv mediante el siguiente comando:

pip install python-dotenv

Después de instalar la dependencia se generó el archivo requirements.txt usando:

pip freeze > requirements.txt

Este archivo almacena todas las librerías necesarias para que otro usuario pueda ejecutar el proyecto correctamente utilizando:

pip install -r requirements.txt

La gestión de dependencias es importante porque facilita compartir proyectos y mantener controladas las versiones de las librerías utilizadas.

# Cómo ejecutar el proyecto

Una vez activado el entorno virtual e instaladas las dependencias, el proyecto se ejecutó desde la terminal con el siguiente comando:

python main.py

El archivo main.py es el punto principal de entrada del sistema y desde allí se ejecuta el menú interactivo de gestión de usuarios. El sistema permite registrar usuarios, listarlos y buscarlos mediante opciones desde consola.

# Explicación de módulos y paquetes

El proyecto fue organizado utilizando módulos y paquetes para mejorar la estructura y el orden del código. Los paquetes son carpetas que contienen archivos **init**.py y permiten agrupar diferentes módulos relacionados.

Dentro del proyecto se creó el paquete “usuarios”, que contiene:

* gestor.py → encargado del registro, listado y búsqueda de usuarios.
* validaciones.py → encargado de validar nombres y edades.

También se creó el paquete “config”, que contiene:

* settings.py → encargado de cargar las variables de entorno.

La modularización permite dividir responsabilidades, reutilizar código y facilitar el mantenimiento del proyecto.

# Uso de variables de entorno

Las variables de entorno se almacenaron en un archivo .env para separar las configuraciones importantes del código principal. En este archivo se definieron variables como:

APP_NAME=Sistema Usuarios
APP_VERSION=1.0
ADMIN_USER=admin

Estas variables fueron cargadas utilizando la librería python-dotenv mediante el archivo settings.py. Gracias a esto, el sistema puede acceder a configuraciones importantes de forma más segura y organizada sin escribir directamente los datos dentro del código fuente.
