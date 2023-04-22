""" El bucle for en Python se utiliza para iterar sobre una secuencia (lista, tupla, cadena), 
u otros objetos iterables. 
La iteración sobre una secuencia se denomina recorrido. La sintaxis de la instrucción es: 

# for elem in secuencia:
#   instrucciones del bucle

Aquí, elem es la variable que toma el valor del elemento dentro de la secuencia en cada iteración. 
La sintaxis incluye in, lo cual indica que son todos los valores dentro de la secuencia. 
Un bucle for puede tener también un bloque else opcional. 
La parte else se ejecuta al agotarse los elementos de la secuencia en el bucle for. """

for i in range(1, 20+1):
    print(i)

# Range y len determinan el indice de los elementos de la secuencia
for i in range(len("Poli")):
    print({i})

################################################################
# ciclos
# ejecutan intrucciones repetitivas hasta que se cumpla una condicion, o se finalice el ciclo o loop

# ciclo for
# for i in data:
#   instrucciones a realizar
frutas = ["Frutilla", "Avocado", "Manzana"]

for i in frutas:
    print(i)

# for i in range(len(data)):
for i in range(1, 6):
    print(i)

# conocemos los elementos
for i in range(len(frutas)):
    print(i)

# conocemos los elementos y la posicion
palabra = "Python"
for i in range(len(palabra)):
    print(palabra[i])
