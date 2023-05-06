def suma(n1, n2, n3):  # definir la función con 3 parametros, 3 num a usar
    """ Función que suma valores en lista """
    # sumatoria de valores
    suma1 = n1+n2+n3
    #
    suma_final = (n1-(n2+n3))
    # retorna una tupla con los resultados de las operaciones
    return (suma1, suma_final)


# Declaracion de una lista con valores
lista = {1, 2, 3}
# Variable que almacena el resultado de la ejecución de la función con los valores de lista
resultado_lista = suma(*lista)
# Imprime tupla que contiene los resultados de las operaciones dentro d ela función
print(resultado_lista)
resultado_tupla = suma(1, 2, 3)
print(resultado_tupla)

# Función Alternativa


def suma2(listado):
    suma_1 = sum(*listado)
    suma_final = listado[0] - (listado[1]+listado[2])

    return (suma_1, suma_final)


print(suma(*lista))
