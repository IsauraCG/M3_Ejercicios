""" Escribir un programa que analice un número, e indique si es positivo o negativo, 
y si es par o impar. En caso de ser cero, también indicarlo. 
Se debe usar la expresión if-elif-else, y no usar subcondiciones; 
en su lugar, usar condiciones anidadas """

# e solicita un numero al usuario
print("Por favor, ingrese un número:")
N = int(input())

# Se establece una sentencia condicional 'IF'
if N > 0:  # Si el numero es mayor que cero, es positivo e imprime eso
    print(f"El número {N} es positivo")
    if N % 2 == 0:  # Establece la condicion de si es divisible por 2, es par
        print("y es par")
    else:  # Si no es divisible por 2, es impar e imprime eso
        print("y es impar")

elif N < 0:  # Si
    print(f"El número {N} es negativo")
    if N % 2 == 0:
        print("y es par")
    else:
        print("y es impar")
else:
    print("El número es '0'")
