lista = []

#lista de opciones para el crud
datos =["g","m","b","s","yes"]

confirmar = input("Bienvenido a tu lista de compra, quieres ver que puedes hacer? Escribe yes para continuar")

if confirmar.lower() == "yes":
#pequeña comprobacion para iniciar el bucle de opciones
    while confirmar.lower() in datos:

        confirmar = input("""Que accion deseas realizar:
                                 g para guardar
                                 m para modificar
                                 b para borrar
                                 s para sair""")
        confirmar = confirmar.lower()

        if confirmar.lower() == datos[0]:
            item = input("Ingrese el nombre del compra: ")
            item = item.lower()
            if item in lista:
                print(f"El producto {item} ya se encuentra en la lista")
            else:
                lista.append(item)
                print(f"El producto {item} se ha agregado a la lista")


        elif confirmar.lower() == datos[1]:
            print(lista)
            item = input("Ingrese el prodcuto a modificar: ")
            item = item.lower()
            while item in lista:
                posicion = lista.index(item)

                new = input("Ingrese el nuevo nombre del producto: ")
                lista[posicion] = new

                print(f"se ha actualizado el {item} en la lista y ahora es {new}")

        elif confirmar.lower() == datos[2]:
            print(lista)
            item.low = input("Ingrese el prodcuto a eliminar: ")
            item = item.lower()
            while item in lista:
                posicion = lista.index(item)

                del lista[posicion]
                print (f"El producto {item} se eliminado en la lista")

        elif confirmar.lower() == datos[3]:
            print(f"La lista final es {lista}")
            break

else:
    print("adios")


