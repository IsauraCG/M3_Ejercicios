# Crear una lista con 10 números enteros, recorrerla haciendo uso de la sentencia for,
# e imprimir en pantalla el valor de cada elemento indicando si es par, impar o cero.

# importa librería para patrones de expresiones regulares
import re

# Se define la variable que almacenará como lista los números ingresados por usuario
nums = []  # lista con numerosingresados
num = ""  # el numero ingresado
patron = re.compile(".*[0-9]")  # compilacion de patron

# Mensaje de Bienvenida
print("Por favor ingrese 10 números enteros, positivos o negativos\n" +
      "No se permiten decimales u otros caracteres que no sean numéricos:")

# establece un ciclo while que se ejecuta mientras la lista no tenga al menos 10 elementos
while len(nums) >= 0 and len(nums) < 10:

    # asignamos el valor a variable num mediante input (ingresado por usuario)
    num = input("Ingresa un número: ")

    if num == " " or num == "":  # condicionar si no se ingresa ningún número o ingresa espacio
        print("No has ingresado nada. Debes Ingresar un número.")
    # condicionar que ' num' ingresado coincida con expresión regular (sólo números)
    elif re.match(patron, num):
        nums.append(num)  # si es un número lo agrega a la lista
    else:  # si no es número envía error
        print("Opción inválida. Ingresa un número")


def imprime_par_impar_cero(lista_val):
    """ Función que determina si los numeros ingresados por usuario, y almacenados en 
    la lista 'nums' , son par, impar o cero """
    lista_val = []  # Declaracion de variable en parámetro de la func.
    for i in lista_val:  # Ciclo For que recorre cada uno de los items en la lista
        if int(i) == 0:  # condiciona si el item en lista es igual a 'cero'
            print("El numero es 0.")  # imprime mensaje 'es cero'
        elif int(i) % 2 == 0:  # condiciona si el item en lista es múltiplo de 2 ( resto == 0)
            print(f"{i} es par.")  # imprime mensaje 'es par'
        else:  # # condiciona si el item en lista no es cero ni par, entonces es impar
            print(f"{i} es impar.")  # imprime mensaje 'es impar'


print("\n================================\nLOS NUMEROS INGRESADOS SON\n")
# Ejecuta función 'imprime_par_impar_cero' con los valores en lista 'nums'
imprime_par_impar_cero(nums)
