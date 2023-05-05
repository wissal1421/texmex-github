import os

# Ruta del archivo recetas.md
ruta_archivo = "recetas.md"

# Abrir el archivo y leer su contenido
with open(ruta_archivo, "r") as archivo:
    contenido = archivo.read()

# Imprimir el contenido del archivo en la terminal
print(contenido)
