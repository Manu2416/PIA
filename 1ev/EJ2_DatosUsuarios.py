"""
Tenemos un fichero csv con datos los siguientes datos de usuarios: username, email, nombre, genero, edad, pais y codigo postal.
Partiendo de este fichero (adjunto a la tarea) realiza las siguientes acciones:

- Carga los datos del fichero

- Crea un objeto (clase o diccionario) para almacenar los datos de cada usuario.

- Crea una carpeta con la letra de cada inicial del username y dentro crea un fichero con los datos del usuario.

- Procesa los datos para crear un objeto por cada una de las lineas y añadirlo a una lista o diccionario

- Realiza un menú en el que se pueda:

    1. Consultar los datos de un usuario buscando por username

    2. Añadir un nuevo usuario con todos sus datos. Se deben validar formato y tipo de dato como sigue: 

- El email debe tener una @ y un punto

- La edad debe ser numérica entera entre 1 y 120

- El genero únicamente puede tomar el valor: masculino, femenino, no binario

- El código postal tendrá como mucho una longitud de 6 dígitos.

    3. Eliminar un usuario, pidiendo el email del mismo.

    4. Salir. Al salir se deben volcar los cambios al fichero. Para ello debemos saber si se han eliminado usuarios. Así definiremos la estrategia de volcado de datos ¿por qué?

"""
from pathlib import Path
import re


if __name__ == "__main__":
    pass
