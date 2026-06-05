""" PRIMER RETO
for a in range(1,101):
    if (a % 5 ==0) and (a % 3 == 0):
        print("fizzbuzz")
    elif a % 3 == 0:
        print("fizz")
    elif a % 5 == 0:
        print("buzz")
    else:
        print(a)"""

"from wsgiref.util import request_uri"

"""  SEGUNDO RETO
a = list(input("coloca una palabra"))
b = list(input("coloca otra palabra"))

if len(a) == len(b):
    for letra1 in a:
        if letra1 in b:
            respuesta = True
            #print(respuesta)
        else:
            print("la palabra no es un anagrama")
            exit()

    if respuesta == True:
        print("la palbara es una anagrama")
else:
    print("No son iguales")"""

""" TERCER RETO
t = 0
p = 1
fibo = int(input("Hola coloca un tope"))
if fibo > 1:
    print(0)
    print(1)
    for a in range(1,fibo+1):
        c = t + p
        t = p
        p = c
        print(c)"""

""" CUARTO RETO

version super complicada por que si
for i in range(1,100):

    if i == 1:
        print(f"El numero {i} no es uno ni otro")
    elif i == 2:
        print(f"El numero {i} es primo")
    elif i > 2:
        lista = list()
        for pete in range(i,1,-1):
            resultado = i % pete
            lista.append(resultado)
            a = lista.count(0)
        if a >= 2:
            print(f"El numero {i} no es primo")
        else:
            print(f"El numero {i} es primo")"""

"""
 solucin corta de comprobacion de primo y no primo
for i in range(1, 100):

    if i < 2:
        print(f"El número {i} no es primo")
        continue

    es_primo = True

    for divisor in range(2, i):
        if i % divisor == 0:
            es_primo = False
            break

    if es_primo == True:
        print(f"El número {i} es primo")
    else:
        print(f"El número {i} no es primo")"""
""" QUINTO RETO
nombre = " "

def area(nombre):

    while nombre != "c" and nombre != "t" and nombre != "r":
        nombre = input(""
                       coloca lo que quieras calcular:
                       [c] para cuadrado
                       [t] para triangulo
                       [r] para un rectangulo
                       "")

    if nombre == "c":
        valor1 = int(input("Ingrese el primer valor"))
        valor2 = int(input("Ingrese el segundo valor"))
        resultado = valor1 * valor2
        print(resultado)
    elif nombre == "r":
        valor1 = int(input("Ingrese el primer valor"))
        valor2 = int(input("Ingrese el segundo valor"))
        resultado = valor1 * valor2
        print(resultado)
    elif nombre == "t":
        valor1 = int(input("Ingrese al valor de la base"))
        valor2 = int(input("Ingrese la altura"))
        resultado = (valor1 * valor2) / 2
        print(resultado)

area(nombre)
"""
"""
poligono = ""
while poligono != "c" and poligono != "t" and poligono != "r":
    poligono = input("Ingrese el tipo de poligono"
                     "c para cuadrado"
                     "t para triangulo"
                     "r para un rectangulo")
if poligono =="c":
    valor1 = int(input("Ingrese el primer valor"))
    valor2 = int(input("Ingrese el segundo valor"))

elif poligono =="t":
    valor1 = int(input("Ingrese el primer valor"))
    valor2 = int(input("Ingrese el segundo valor"))

elif poligono =="r":
    valor1 = int(input("Ingrese el primer valor"))
    valor2 = int(input("Ingrese el segundo valor"))

def areas(poligono, valor1, valor2):
    if poligono == "c":
        return(valor1 * valor2)
    elif poligono == "t":
        return((valor1 * valor2)/ 2)
    elif poligono == "r":
        return(valor1 * valor2)
resultado=areas(poligono, valor1, valor2)
print(resultado)
"""

""" tengo problemas la verdad
print (a , b)
resultado = imagen.size[0] /b
resultado2 = imagen.size[1] /b
print(resultado)
print(resultado2)
"""

"""
def mdc (a,b):
    while a > 0:
        rest = a % b
        a = b
        b = rest
        if rest == 0:
            break
    print(f"el mdc es {a}")
    return a

import requests
from PIL import Image
from io import BytesIO

hito = 'https://images.ctfassets.net/s699s7kh1jys/2OBtP7Nm4xs6A8fOofS12A/daa5e1e035bebea10b401a65d54ced80/Detail_of_side_rear_view_of_Porsche_911_GT3_RS__type_991.1__on_road_in_Guards_Red_in_Scottish_countryside_new.jpg'
response = requests.get(hito)
response.raise_for_status()
imagen = Image.open(BytesIO(response.content))

a = imagen.size[0]
b = imagen.size[1]


pete = mdc(a,b)

t = int(a / pete)
p = int(b /pete)
print(f"El aspect ratio es de {t}:{p}")
"""

"""while a < 0:
    print(a)
    print(cadena[a+1])
    a += 1"""

"""
cadena = input("Coloca lo que quieres revertir: ")
a = len(cadena)

lista = list()
while a > 0:
    lista.append(cadena[a-1])
    a -=1
final = "".join(lista)
print(final)
"""

"""
texto = input("Ingrese un texto: ").lower()
raros = [',','"','(',')','.']

for caracter in texto:
    if caracter in raros:
        texto = texto.replace(caracter,"")
#print(texto)
palabra = texto.split()
nueva_lista = []

for a in palabra:
    pt = palabra.count(a)



    if pt > 1:
        if a not in nueva_lista:
            print(f"La palabra {a} esta {pt} veces")
            p = nueva_lista.append(a)
        else:
            continue



    else:
        print(f"La palabra {a} esta {pt} veces")
"""

"""
numero = int(input("Ingrese un numero: "))
lista = list()
while numero >= 1:
    a = int(numero / 2)
    b = numero % 2
    lista.append(b)
    numero = a

lista.reverse()
resul = "".join(map(str,lista))
print(resul)
"""

"""
my_dict = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---",
           "k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
           "u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."," ":""}
lista1 = my_dict.keys()
lista2 = my_dict.values()

#print(my_dict[" "])
palabra = input("Ingrese una palabra: ").lower().strip()

#print(palabra.split(' '))

if palabra[0] in lista1 or palabra[0] in lista2:

    if palabra[0] in lista1:
        for caracter in palabra:
            if caracter in my_dict.keys():
                print(my_dict[caracter],end=" ")




    elif palabra[0] in lista2:
        for index in palabra.split(' '):
            for clave, index2 in my_dict.items():
                if index == index2:
                    clave_found = clave
                    print(clave_found,end="")

"""
"""
my_dict = {"{":"}","[":"]","(":")"}

texto = input("Ingrese la expresion a revisar: ")

comprobacion = list()

for caracter in texto:
    if caracter in my_dict.keys():
        posicion1 = list(my_dict.keys()).index(caracter)
        comprobacion.append(posicion1)

    if caracter in my_dict.values():
        posicion2 = list(my_dict.values()).index(caracter)

        if comprobacion == []:
            print("formato no valido")
            break
        elif posicion2 == comprobacion[-1]:
            comprobacion.pop()


        else:
            print("La espresion no esta balanceada")
            break

else:
    if comprobacion == []:
        print("La espresion esta balanceada")
    else:
        print("La espresion no esta balanceada")
"""

"""
def cadenas(str1, str2):
    out1 = ""
    for caracter in str1:
        if caracter in str2:
            continue
        else:
            out1 += caracter
    print(out1)

    out2 =""
    for caracter in str2:
        if caracter in str1:
            continue
        else:
            out2 += caracter
    print(out2)

str1 = input("Ingresa una cadena de caracteres")
str2 = input("Ingresa otra cadena de caracteres")

cadenas(str1, str2)
"""
"""
def reversado (cadena):
    puntuacion = [
        ".", ",", ";", ":", "¿", "?", "¡", "!",
        "(", ")", "[", "]", "{", "}",
        "\"", "'", "«", "»",
        "-", "–", "—", "_",
        "…", "/", "\\", "|",
        "@", "#", "$", "%", "&", "*", "+", "=",
        "<", ">"]

    acentuacion = {"á":"a","é":"e","í":"i","ó":"o","ú":"u"}

    a = ""
    cadena = cadena.replace(" ","")
    new_cadena=""
    for item in cadena:
        if item in puntuacion :
            new_cadena += ""
        elif item in acentuacion.keys() :
            new_cadena += acentuacion[item]

        else:
            new_cadena += item

    
    for item in reversed(new_cadena):
        a += item

    if a == new_cadena:
        return True
    else:
        return False


cadena = input("Ingresa una cadena de caracteres").lower().strip()


print(reversado(cadena))

"""
"""
def factorial (numero):

    if numero < 0:
        return ("No existe")

    elif numero <= 1:
        return 1
    else:
        return numero * factorial(numero -1)


numero = int(input("Ingrese un numero: "))
print(factorial(numero))
"""
"""
def armstrong (numero):
    acumulacion = 0
    potencia = len(numero)
    for i in numero:
        a = int(i)
        a = pow(a, potencia)
        acumulacion = acumulacion + a
    total = str(acumulacion)

    if total == numero:
        return " es un numero de amstrong"
    else:
        return " no es un numero de amstrong"

numero = input("Ingrese un numero: ")
print(armstrong(numero ))

"""

""" intento fallido
import re

def calculadora(fecha, fecha2):
    fechas = {1:range(1,31), 2:range(1,28), 3:range(1,31), 4:range(1,30), 5:range(1,31),
              6:range(1,30), 7:range(1,31), 8:range(1,31), 9:range(1,30), 10:range(1,31)
             , 11:range(1,30), 12:range(1,31)}
    lista1 = list()
    lista2 = list()

    for item in fecha.split("/"):
        a = int(item)
        lista1.append(a)

    if lista1[1] in fechas.keys() and lista1[0] in fechas[lista1[1]]:
        a = 1
    else:
        print("fecha fuera de rango")


    for item in fecha2.split("/"):
        b = int(item)
        lista2.append(b)

    if lista2[1] in fechas.keys() and lista2[0] in fechas[lista2[1]]:
        a = 1
    else:
        print("fecha fuera de rango")

    if lista1[2] > 0 and lista2[2] > 0:

        res_dia = lista1[0] - lista2[0]
        res_mes = lista1[1] - lista2[1]
        res_year = lista1[2] - lista2[2]
        res_bic = int(res_year / 4)

        year = res_year * 365
        month = res_mes * 30
        total_days = year + month + res_dia + res_bic

    return(print(total_days))



fecha = ""
fecha2 = ""



while not  re.match(patron, fecha):
    fecha = input("ingrese la primera fecha con el formato dd/mm/aaaa:  ")

while not re.match(patron, fecha2):
    fecha2 = input("ingrese la segunda fecha con el formato dd/mm/aaaa:  ")

calculadora(fecha, fecha2)

"""
"""
diccionario = {1:list(range(1,31)),2:list(range(2,20))}

a = int(input("ingrese la primera cadena de caracteres: "))
lista = [25,a]

if lista[1] in diccionario.keys():
    if lista[0] in diccionario[lista[1]]:
        print("se encontro el valor")
    else:
        print("no esta")
"""
"""
from datetime import datetime

def calculadora(fecha1, fecha2):
    if fecha1 == fecha2:
        print("Son la misma fecha")
    elif fecha1 > fecha2:
        resultado = fecha1 - fecha2
    else:
        resultado = fecha2 - fecha1

    return(resultado)



fecha = input("Ingresa una fecha")
fecha1 = datetime.strptime(fecha, "%d/%m/%Y")

fecha = input("ingresa la segunda fecha")
fecha2 = datetime.strptime(fecha, "%d/%m/%Y")

print(calculadora(fecha1, fecha2))
#if re.match(patron, fecha1):
#    print("no se ni lo que estoy haciendo xd ")
"""

"""
def fechas(texto):
    new_texto = " ".join(texto.split())
    print(new_texto)
    for palabra in new_texto.split(" "):
        letra = palabra[0].upper()
        palabra[0] = letra

        print(palabra)


texto = input("Ingresa lo que te flote el barco: ")
fechas(texto)
"""

"""def recorrido(acciones, pista):
    newcadena = ""
    if len(acciones) == len(pista):
        for i, accion in enumerate(acciones):
            if accion == "jump" and pista[i] == "|":
                newcadena += "|"
            elif accion == "run" and pista[i] == "_":
                newcadena += "_"
            elif accion == "run" and pista[i] == "|":
                newcadena += "/"
            elif accion == "jump" and pista[i] == "_":
                newcadena += "x"
        if newcadena == pista:
            return (newcadena, True)
        else:
            return (newcadena, False)
    else:
        return ("los tamaños no coinciden")

acciones = ["jump", "run", "run", "jump"]
pista = "|___"

print(recorrido(acciones, pista))"""

"""
def recorrido(acciones, pista):
    if len(acciones) != len(pista):
        return ("Los tamaños no coinciden", False)

    resultado = ""
    success = True

    for accion, tramo in zip(acciones, pista):
        if (accion == "run" and tramo == "_") or (accion == "jump" and tramo == "|"):
            resultado += tramo  # correcto
        elif accion == "run" and tramo == "|":
            resultado += "/"
            success = False
        elif accion == "jump" and tramo == "_":
            resultado += "x"
            success = False

    return (resultado, success)


acciones = ["jump", "run", "run", "jump"]
pista = "|___"

print(recorrido(acciones, pista))

"""

matriz = [
    ["o", "x", "x"],
    ["x", "x", ""],
    ["o", "o", ""]
]
nuevamatriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

conteox = 0
conteoo = 0

for i, fila in enumerate(matriz):
    for j, columna in enumerate(fila):
        print(i, j)
        if columna == "x":
            nuevamatriz[i][j] = True
            conteox += 1


        elif columna == "o":
            nuevamatriz[i][j] = False
            conteoo += 1
        else:
            nuevamatriz[i][j] = ""

if conteox - conteoo == 1 or conteox - conteoo == 0:
    print("valores validos")


else:
    print("no validos")

if all(nuevamatriz[0]) or all(nuevamatriz[1]) or all(nuevamatriz[2]):
    print("gana la x  en horizontal")

elif all((nuevamatriz[0][0], nuevamatriz[1][1], nuevamatriz[2][2])) or all(
        (nuevamatriz[0][2], nuevamatriz[1][1], nuevamatriz[2][0])):
    print("gano la x en diagonal")

elif not any((nuevamatriz[0][0], nuevamatriz[1][1], nuevamatriz[2][2])) or not any(
        (nuevamatriz[0][2], nuevamatriz[1][1], nuevamatriz[2][0])):
    print("gano la o en diagonal")

elif not any(nuevamatriz[0]) or not any(nuevamatriz[1]) or not any(nuevamatriz[2]):
    print("gano el o en horizontal ")

elif all((nuevamatriz[0][0], nuevamatriz[1][0], nuevamatriz[2][0])) or all(
        (nuevamatriz[0][1], nuevamatriz[1][1], nuevamatriz[2][1])) or all(
        (nuevamatriz[0][2], nuevamatriz[1][2], nuevamatriz[2][2])):
    print("gano el x en vertical")
elif not any((nuevamatriz[0][0], nuevamatriz[1][0], nuevamatriz[2][0])) or not any(
        (nuevamatriz[0][1], nuevamatriz[1][1], nuevamatriz[2][1])) or not any(
        (nuevamatriz[0][2], nuevamatriz[1][2], nuevamatriz[2][2])):
    print("gano el o en vertical")
else:
    print("no gano nadie")

print(matriz)
print(nuevamatriz)

"""
ingreso = (input("Coloca la logitud de las ramas para comprobar si se puede o no armar un cuadrado: "))
succes = 0
if len(ingreso) > 4 :
    print("No se puede armar el cuadrado")
elif len(ingreso) == 4 :
    for numero, i in enumerate(ingreso):
        if i == ingreso[numero - 1]:
            succes = True


        else:
            succes = False
            
            break

print(succes)
"""
