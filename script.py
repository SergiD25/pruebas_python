"""
password_file = open('Secret_password.txt')
secret_password = password_file.read()
print('Enter your password')
typed_password = input()
if typed_password == secret_password:
    print('Felicidades abriste un archivo por medio de codigo (inutil)')
elif(typed_password == '1234'):
    print('Anormal de carrito')
else:
    print("No parse, no es")
"""

"""
a = 1280
b = 720


while a >0:
    rest  = a % b
    a = b
    b = rest

    print(b, rest , a)
    if rest == 0:
        break
print (f"el mdc es {a}")
"""
"""
a = input("a")

cad = len(a)
while cad>0:
    print(a[cad-1])
    cad -= 1

"""

lista = list()
print(lista)