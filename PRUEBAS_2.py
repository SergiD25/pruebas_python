import os
import datetime

ruta = r"\\172.16.2.252\contenedor\HOJAS DE VIDA GENERAL"

print(f"revisando ruta {ruta}")
my_lista = list()

for tipo_archivo in os.listdir(ruta):
    ruta_completa = os.path.join(ruta, tipo_archivo)

    #if os.path.isfile(ruta_completa):
        #print(f"Esta el siguiente documento {ruta_completa}")
    if os.path.isdir(ruta_completa):
        #print(f"La ruta de la hoja de vida es la siguiente {ruta_completa}")

        my_lista.append(ruta_completa)

    else:
        print("es otro tipo de documento")

    tiempo_de_la_modificacion = os.path.getmtime(ruta_completa)

    fecha_modificacion = datetime.datetime.fromtimestamp(tiempo_de_la_modificacion)

    fecha_legible = fecha_modificacion.strftime("%d/%m/%Y %H:%M:%S")

    #print(f"[{tipo_archivo}] {tipo_archivo}: Fecha de modificacion {fecha_legible}")
print(len(my_lista))