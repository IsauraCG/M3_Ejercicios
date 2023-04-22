""" Escribir un programa que analice un número, e indique si es positivo o negativo, 
y si es par o impar. En caso de ser cero, también indicarlo. 
Se debe usar la expresión if-elif-else, y no usar subcondiciones; 
en su lugar, usar condiciones anidadas """

N = 53

if N > 0:
    print(f"El número {N} es positivo")
    if N % 2 == 0:
        print("y es par")
    else:
        print("y es impar")

elif N < 0:
    print(f"El número {N} es negativo")
    if N % 2 == 0:
        print("y es par")
    else:
        print("y es impar")
else:
    print("El número es '0'")
