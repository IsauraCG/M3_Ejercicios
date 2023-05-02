# Se tiene la siguiente lista de números:

lista_nums = [3, 5, 2, 8, 1, 10]

# Calcular la suma de todos los números de la lista utilizando un bucle while.

i = 0  # se declara iterador de la lista para el indice
sumandos = 0  # declara variable que acumula el valor sumado

# condiciona que mientras el iterador 'i' sea menor al largo de la lista se ejecute el ciclo.
while i < len(lista_nums):
    sumandos += lista_nums[i]
    i += 1

print(f"El valor de la suma de los números {lista_nums} es: {sumandos}")
