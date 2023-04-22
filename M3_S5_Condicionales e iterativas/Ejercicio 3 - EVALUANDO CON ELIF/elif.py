""" Creemos un programa que verifique si un número es positivo, cero o negativo. Para ello debemos
chequear primero si es positivo, y de no ser así, si es igual a cero. En caso de que no cumpla ninguna
de las 2 verificaciones, ya sabemos que el número es negativo. Utilizaremos una sentencia if–elifelse.
"""
num = 3
if num > 0 :
    print(num, "es positivo")
elif num == 0 :
    print(num, "es igual a cero")
else :
    print(num, "es negativo")
#Resultado: 3 es positivo