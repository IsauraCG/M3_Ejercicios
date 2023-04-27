# buscar numeros
buscar = 3
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    # print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
    else:
        print("no encontrado")
