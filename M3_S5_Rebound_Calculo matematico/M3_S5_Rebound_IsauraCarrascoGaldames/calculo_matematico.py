""" Requerimos calcular el factorial de un número, asignarlo a una variable, y luego imprimirla.
Sabiendo que el factorial es el resultado de la multiplicación de todos los enteros positivos que hay
entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1. """

num = 9
i = 0
factorial = 1
while num > 0 and i < num:
    i = i+1
    factorial = factorial * i
    #print(f"i = {i} , fact = {factorial}")
print(f'\nEl FACTORIAL de {num}, se expresa como {num}! \ny su valor es: {factorial}')
#   n! = 1 * 2 * 3 * 4 * ... * (n-1) * n 

