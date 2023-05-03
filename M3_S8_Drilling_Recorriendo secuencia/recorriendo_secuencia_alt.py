# Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
lista_de_listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

# Hay que imprimir cada dato de las listas en pantalla con las siguientes excepciones:
#   • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista,
#   • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.
#   • Adicionalmente, crear un diccionario donde asignaremos la primera sublista a la clave A, la
#      segunda a la clave B, la tercera a la clave C, y la cuarta a la clave D.
#   • Finalmente, imprimiremos en pantalla el diccionario resultante.
#
#   Ejemplo de impresión en pantalla:
#   A:[1, 2, 3]

################################

diccionario = dict()
otro_diccionario = dict()
claves = ['A', 'B', 'C', 'D']
# contador
i = 0

for element in lista_de_listas:

    if element[0] == 0:
        continue
    for num in element:
        if num == 0:
            element.remove(num)
            continue
        print(num)
    i += 1  # aumenta contador
    # asigna el valor de 'element' a cada key
    # que, a su vez, se compone de un elemento en la lista 'claves',
    # cuyo índice es el que le asigna el 'contador' (i),
    # asignado por el valor de cada vuelta del ciclo for
    # diccionario[key] = [valor]
    diccionario[claves[i]] = element

    # otro_diccionario[key] = [value]
    # [key] = claves[indice]   ----
    #                   =>> [indice] = lista_de_listas.index(element)
    #                    =>> indice  = el índice que tiene 'element' (sublista) en 'lista_de_listas'
    # [value] = element  ---- "la sublista"
    otro_diccionario[claves[lista_de_listas.index(element)]] = element

print(diccionario)
print(otro_diccionario)
