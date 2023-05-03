# Crear una función que acepte 3 números como parámetros, sume todos los valores,
# y adicionalmente, reste el segundo y tercer parámetro al primero.
# Al invocar la función, debemos pasarle los parámetros en forma de lista.
# Esta devolverá ambos resultados en una tupla.
# Los resultados se deben imprimir en pantalla.

########################################################################

# Se declaran las variabes que solicitan el ingreso al usuario
param1 = input("Ingrese un numero: ")
param2 = input("Ingrese un 2° numero: ")
param3 = input("Ingrese un 3° numero: ")

# se almacenan ly parsean los datos recibidos en una lista
lista_param = [int(param1), int(param2), int(param3)]

# se define la funcion según los requerimientos


def func_aritmeticas(lista):
    """ Funciones aritmeticas """
    # declaración de variables locales
    sumar = 0
    restar = 0
    tupla = ()
    # ciclo para realizar la suma de manera iterativa
    for param in lista:
        sumar = param + sumar
    # impresión de la suma
    print(f"\nEl resultado de la suma de los números es: {sumar}\n")

    # operación restar os dos siguientes al priemro
    restar = lista[0] - (lista[1] + lista[2])
    # impresión de la resta
    print(f"El resultado de restar los dos últimos al primero : {restar}\n")
    tupla = (sumar, restar)
    # asignación de los valores de retorno
    return tupla


print(f"La tupla resultante es: {func_aritmeticas(lista_param)}\n")
