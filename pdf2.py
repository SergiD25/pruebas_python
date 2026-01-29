eliminar = {'P', 'T', 'G', 'F', 'C', 'N', 'B', 'O'}

with open("tareas.txt", "r") as f:
    for linea in f:
        resultado = ''.join(c for c in linea.strip() if c not in eliminar)
        print(resultado)
