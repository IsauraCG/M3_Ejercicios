numeros = input('ingrese 3 numeros distintos separados por coma (,) :')
numeros = [int(i) for i in numeros.split(',')]  # identifica separador de coma


def check_length_three(num: list) -> bool:
    """ funcion que checkea que la lista de numeros tenga 3 elementos """
    if len(num) == 3:
        return True
    else:
        return False


def check_no_distintos(num: list) -> bool:
    """ función que checkea que los numeros sean distintos """
    if num[0] != num[1] and num[0] != num[2] and num[1] != num[2]:
        return True
    else:
        return False


def sort_no(num: list) -> list:
    """ función que sort (ordena) con método 'sorted' la lista de números,
    y la opción reverse =True, hace que liste los números de mayor a menor."""
    # print(num)
    return sorted(num, reverse=True)


while check_length_three(numeros) == False or check_no_distintos(numeros) == False:
    numeros = input(
        'Los numeros no son distintos\n'
        'Debe ingresar 3 números distintos separados por coma (,) :')
    numeros = [int(i) for i in numeros.split(',')]


# print("Numeros seleccionados: ")
# print(*numeros, sep=', ')
numeros = sort_no(numeros)
print("Los números son diferentes entre sí, y ordenados de mayor a menor son: ")
print(*numeros, sep=', ')
