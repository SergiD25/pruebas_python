
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
from itertools import count

"from wsgiref.util import request_uri"

""" a = list(input("coloca una palabra"))
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

"""t = 0
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



""" version super complicada por que si
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


""" solucin corta de comprobacion de primo y no primo
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
"""
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








