logo = """
 _____________________
|  _________________  |
| | Bootcamp Python | | 
| |_________________| | 
|  ___ ___ ___   ___  | 
| | 7 | 8 | 9 | | + | | 
| |___|___|___| |___| | 
| | 4 | 5 | 6 | | - | | 
| |___|___|___| |___| | 
| | 1 | 2 | 3 | | x | | 
| |___|___|___| |___| | 
| | . | 0 | = | | / | | 
| |___|___|___| |___| |   
|_____________________|
"""

def suma(a, b):
    """
    Suma a + b
    :param a: primer valor
    :param b: segundo valor
    :return: resultado
    """
    return a + b


def resta(a, b):
    """
    Suma a - b
    :param a: primer valor
    :param b: segundo valor
    :return: resultado
    """
    return a - b


def multiplicacion(a, b):
    """
    Multiplica a * b
    :param a: primer valor
    :param b: segundo valor
    :return: resultado
    """
    return a * b


def division(a, b):
    """
    divide a / b
    :param a: primer valor
    :param b: segundo valor
    :return: resultado
    """
    return a / b

operador = {
            "+": suma,
            "-": resta,
            "*": multiplicacion,
            "/": division
            }
print(logo)
num1 = int(input('Ingresa el primer número '))
num2 = int(input('Ingresa el segundo número '))
for k in operador:
    print(k)
simbolo = input("Escoge el operador ")
resultado = operador[simbolo]

print(f'{num1} {simbolo} {num2} = {resultado(num1, num2)} ')