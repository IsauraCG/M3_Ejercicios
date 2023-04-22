""" Eliminar todas las vocales de la palabra “paralelepípedo”, e imprimir en pantalla las
consonantes restantes y su posición dentro de dicha palabra. """

list_palabra = []

for val in "paralelepípedo":
    if val == "a" or val =="e" or val == "í" or val == "o" or val == "u":
        continue
    list_palabra.append(val)
print(f"\nAl imprimir la palabra 'paralelepípedo' sin vocales queda:\n{list_palabra}")
