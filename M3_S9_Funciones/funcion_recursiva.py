
""" FUNCIONES RECURSIVAS
La función se llamará a ella misma hasta que el resultado sea 1.  """


def factorial(x):
    """ función recursiva para el cálculo de un número factorial. """
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)


num = 3
print("El factorial de", num, "es", factorial(num))
# Resultado:
# El factorial de 3 es 6
