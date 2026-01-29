import os

folder = r"\\172.16.2.251\Escaner"

with open("hola.txt", "r") as f:
    for linea in f:
        numero = linea.strip()
        nombre = f"mdc.{numero}.pdf"
        ruta_total = os.path.join(folder, nombre)

        if os.path.exists(ruta_total):
            print(f"El archivo {nombre} si esta")
        else:
            print(f"El archivo {nombre} no existe")