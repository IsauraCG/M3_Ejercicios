# Encontrar los repetidos en la siguiente lista

lista = [45, 23, 67, 89, 12, 56, 78, 90, 45, 67, 12, 45, 67, 67, 12, 12, 12]
# arreglo que acumula los elementos repetidos
repetidos = []
# set que acumula una vez cada elemento repetidos.
set_repetidos = set(repetidos)

for num in lista:  # ciclo que recorre la lista de números, indicando 'por cada numero en lista: ejecutar ...'
    # condiciona que al 'contar' los elementos, si su contador es mayor a 1, ese 'num' es 'repetidos'
    if lista.count(num) > 1:
        # si es numero repetido, lo añade a la lista 'repetidos' que los acumula durante el ciclo
        repetidos.append(num)

# Fuera del ciclo, la lista de repetidos se añaden a un 'set' o 'conjunto' de elementos repetidos,
# para mostrarlos una vez
set_repetidos.update(repetidos)

# Una vez obtenidos los valores de los números que se repiten se imprimen en consola
print("Los elementos repetidos son: ")
print(*set_repetidos, sep=', ')

# Si queremos imprimir cuántas veces se repite cada elemento repetido:
for num in set_repetidos:
    print(f"El elemento {num} se repite {lista.count(num)} veces.")
