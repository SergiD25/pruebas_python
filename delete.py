import os
from unittest import skip

with open("tareas.txt", "r") as f:
    for linea in f:
        numero = linea.strip()
        my_list = list(numero)
        eliminar = ['P','T','G','F','C','N','B']

        for num in my_list:
            after = num
            if after in eliminar:
                del after
                after = ''

            print(after)