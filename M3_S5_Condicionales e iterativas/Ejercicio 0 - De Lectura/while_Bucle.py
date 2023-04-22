""" El bucle while en Python se utiliza para iterar sobre un bloque de código mientras la expresión 
de prueba (condición) sea verdadera. 
Generalmente, utilizamos este bucle cuando no sabemos de antemano el número de veces que hay que iterar. 
Sintaxis del bucle while: """

# while expresión_de_prueba:
#   Cuerpo del while

# ciclo while

# ciclo while(condicion) condicion siempre se evaliua True al menos se cambie

i = 0
while i <= 5:
    i += 1  # contador
    print(f"Imprimiendo el valor de i {i}")

"""En el bucle while, la expresión_de_prueba se comprueba primero. 
Cuerpo del while se correrá sólo si la expresión_de_prueba se evalúa como True. 
Después de una iteración, la expresión de prueba se comprueba de nuevo. Este proceso continúa hasta que la 
expresión_de_prueba sea falsa. 
En Python, el cuerpo del bucle while se determina mediante la indentación. 
El cuerpo comienza con sangría, y la primera línea sin sangría marca el final. 
Python interpreta cualquier valor distinto de cero como True. Ninguno y 0 se interpretan como Falso.

La sentencia break termina el bucle que la contiene. 
El control del programa fluye hacia la sentencia inmediatamente posterior al cuerpo del bucle. 
Si la sentencia break está dentro de un bucle anidado (bucle dentro de otro bucle), la sentencia break terminará 
el bucle más interno. Sintaxis de break: """

# Break

i = 0
while i <= 5:
    i += 1  # contador
    if i == 4:
        break
    print(f"Imprimiendo el valor de i {i} y probando el break")

while True:
    print("Palabra")
    break

"""La sentencia continue se utiliza para saltar el resto del código dentro de un bucle sólo para la iteración actual. 
El bucle no termina, sino que continúa con la siguiente iteración. Sintaxis de continue: """

# continue

i = 0
while i <= 5:
    i += 1  # contador
    if i == 1:
        continue
    print(f"Imprimiendo el valor de i {i} y probando continue")
