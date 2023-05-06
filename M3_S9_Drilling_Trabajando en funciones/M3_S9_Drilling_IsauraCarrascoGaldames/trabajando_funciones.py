# Crear una función que sume dos números, otra que reste dos números,
#  otra que multiplique dos números, y otra que divida dos números.
#
# Adicionalmente, crear una función que acepte dos números como parámetros
# y regrese el resultado en forma de tupla de su suma, resta, multiplicación y división.
# Ej: tupla = (suma, resta, multiplicación, división)

# Los resultados se deben almacenar en un diccionario,
# cuyas claves serán: 'Suma', 'Resta', 'Multiplicación', 'División'
# y los valores de cada clave serán:
# los resultados obtenidos con la función creada anteriormente.

# Ejm: dict = {'Suma' : suma}
# =>> dict = {'Suma' : tupla[0]}
# =>> dict['Suma] = tupla[0]

# Se definen al funciones a utilizar

# Funcion suma
def sumar(n1, n2):
    suma = n1 + n2
    return suma

# Función resta


def restar(n1, n2):
    resta = n1-n2
    return resta

# Función multiplicar


def multiplicar(n1, n2):
    multiplicacion = n1 * n2
    return multiplicacion

# Función división


def dividir(n1, n2):
    division = n1 // n2
    return division

# Función que crea uan tupla con los resultados de las funciones anteriores


def tuplación(n1, n2):
    tupla_resultado = tuple((sumar(n1, n2), restar(n1, n2),
                             multiplicar(n1, n2), dividir(n1, n2)))
    # return (sumar(n1, n2), restar(n1, n2), multiplicar(n1, n2), dividir(n1, n2))
    return tupla_resultado


# Declaración de variables ppara asignar valores a operar
a = b = 0
t = True

# Ciclo para solicitar valores positivos
while True:
    # Solicitar valores para operar
    a = int(input("\nIngresa un 1° número para operar (A): "))
    b = int(input("\nIngresa un 2° número para operar (B): "))
    # Condiciona si los numeros son positivos, si es así ejecuta función tuplación (formar tupla)
    if a > 0 and b > 0:
        # Formar tupla
        tupla = tuplación(a, b)

        # Formar diccionario
        dict_resultado = {
            "Suma": tupla[0],
            "Resta": tupla[1],
            "Multiplicación": tupla[2],
            "División": tupla[3]
        }
        # Imprimir Tupla y diccionario
        print(f"\nLa tupla resultante de operar con 4 y 2 es: {tupla}")
        print(
            f"\nUn diccionario resultante de estos valores sería:\n{dict_resultado}\n")

        # Impresion de resultados por separado
        # print(f"El resultado de función sumar es: {tupla[0]}")
        # print(f"El resultado de función restar es: {tupla[1]}")
        # print(f"El resultado de función multiplicar es: {tupla[2]}")
        # print(f"El resultado de función dividir es: {tupla[3]}")

        # Quiebre del ciclo
        break

    else:
        print("\n###################\nPOR FAVOR INGRESA VALORES POSITIVOS > 0\n###################")
