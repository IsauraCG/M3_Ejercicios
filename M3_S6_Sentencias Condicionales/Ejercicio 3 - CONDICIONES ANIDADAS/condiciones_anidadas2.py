""" Requerimos verificar primero si un número es mayor o igual a cero. Si es así, necesitamos
chequear si es igual a cero o mayor que cero (positivo), e imprimir en pantalla el resultado. 
En caso de que el número sea negativo, también debemos imprimir el resultado en pantalla.
Creamos una variable que llamaremos NUM, y le asignaremos como valor el número que deseamos
chequear, en este caso probaremos el número 4. """

NUM = 4

# A continuación, comprobaremos si el número es mayor o igual a cero. Recordemos respetar
# la sintaxis

if NUM >= 0:
    if NUM == 0:
        print("Cero")
    else:
        print("Número positivo")
else:
    print("Número negativo")

# Ahora, haciendo uso del else para el condicional exterior, indicaremos qué sucede si el número
# es negativo. Debemos verificar que la indentación esté al mismo nivel del if exterior
