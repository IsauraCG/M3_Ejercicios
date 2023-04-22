# OPERADORES LÓGICOS

# El resultado de una operación lógica es true o false.
# True cuando la sentencia es verdadera, y false cuando esta es falsa.
x = True
y = False

# And devuelve true cuando ambos elementos son verdaderos, de lo contrario devuelve falso.
print('x and y es: ', x and y,
      ' , FALSE porque los elementos no son -ambos TRUE- o bien, -ambos FALSE-')

# Or devuelve true cuando alguno de los elementos es verdadero, de lo contrario devuelve falso.
print('x or y es: ', x or y, ' , TRUE porque uno de los elementos es verdadero')

# Not devuelve true cuando la sentencia es falsa, o false cuando la sentencia es verdadera.
# Es decir, devuelve el resultado contrario a la sentencia.
print('not y es: ', not y, ' , TRUE porque originalmente -y- es FALSE')

# operadores logicos
# and or not
# evaluar bool o booleanos True or False
a = True
b = False

print(a and b)  # False, deben cumplirse las dos condiciones
print(a or b)  # True, debe cumplirse alguna de las condiciones
print(not a)  # False, not cambia el valor de la condicion
print(not (a or b))  # False
print(not (a and b))  # True
print("-----------------------------------")

# operadores de comparacion
# comparacion de numeros, tamaños, verificar contadores o iteradores
c = 10
d = 5

print(c < d)  # False, menor que
print(c > d)  # True, mayor que
# print(a > b) #True
# print(a < b) #False
print(c <= d)  # False, menor igual que
print(c >= d)  # True, mayor igual que
print(c == d)  # False, igual que
print(c != d)  # True, distinto que
