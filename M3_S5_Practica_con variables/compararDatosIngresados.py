""" 
Pedir el ingreso de dos textos al usuario por consola y comparar si son iguales o del mismo tamaño
"""

textoA = input("Por favor, un texto: ")
textoB = input("Ingreso otro texto: ")

if len(textoA) == len(textoB):
    if textoA == textoB:
        print("Textos iguales y misma longitud")
    else:
        print("Textos diferentes, pero misma longitud")
else:
    print("Textos diferentes")

#### OTRA FORMA ####
# if len(texto1) == len(texto2):
#   print("Textos del mismo tamaño")
# elif texto1 == texto2:
#   print("Textos iguales")
# else:
#   print("Textosdiferentes")
