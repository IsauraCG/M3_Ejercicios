""" Requerimos calcular el FACTORIAL de un número, asignarlo a una variable, y luego imprimirla.
Sabiendo que el FACTORIAL es el resultado de la multiplicación de todos los enteros positivos 
que hay entre un número y uno. Ejemplo: Factorial de 4 es 4 * 3 * 2 * 1. """

# Se solicita un número a evaluar
print("Por favor, ingrese un número:")
N = int(input())

# Se declaran las variables para indice de iteración y el valor del factorial
i = 0
FACTORIAL = 1

# Se establece ciclo while que se ejecuta mientras el número sea mayor a '0'
# y mientras el valor de 'i' sea menor al número
while N > 0 and i < N:
    i = i+1
    FACTORIAL = FACTORIAL * i
    # print(f"i = {i} , fact = {FACTORIAL}") # print que muestra los valoresd e 'i' y 'FACTORIAL'
print(
    f'\nEl FACTORIAL de {N}, se expresa como {N}!\ny su valor es: {FACTORIAL}')
#   n! = 1 * 2 * 3 * 4 * ... * (n-1) *  # Fórmula matemática de factoria
