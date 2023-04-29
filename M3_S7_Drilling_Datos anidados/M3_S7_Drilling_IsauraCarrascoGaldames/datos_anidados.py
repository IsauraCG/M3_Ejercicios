# Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
listas_anidadas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
# Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
#   • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista.
#   • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero

# Se declara variable tipo lista para contener las listas filtradas
filtradas = []
# Se declara una variable tipo lista que contenga los datos filtrados
filtrados = []


def filtrar_listas(anidadas, sublistas_filtradas, numeros_filtrados):
    """ función que realiza el filtro de datos y sublistas """
    # Se establece ciclo for que recorre cada lista del elemento 'listas_anidadas'
    for lista in anidadas:
        # condiciona que si al sublista empieza distinta de '0' pase al ciclo de impresión
        if lista[0] != 0:
            # se añade la sublista y sus elementos al arreglo 'filtradas'
            sublistas_filtradas.append(lista)
            # declara ciclo que recorre cada elemento 'num' en la sublista 'lista'
            for num in lista:
                # condiciona que si el 'num' en 'lista' es distinto de '0' se añade a la lista filtrados
                if num != 0:
                    numeros_filtrados.append(num)
                # si num es igual a 0 , se remueve de la sublista
                elif num == 0:
                    continue

        # condiciona que no se imprima la sublista, si el primer elemento es '0'
        elif (lista[0]) == 0:
            continue

    return numeros_filtrados, sublistas_filtradas


filtrar_listas(listas_anidadas, filtradas, filtrados)

print("\nLos datos que se han filtrado son: ")
print(*filtrados, sep=", ")
print("\nLas sublistas que no comienzan con '0' son:", *filtradas)

for sublista in filtradas:
    if 0 in sublista:
        sublista.remove(0)

print("\nLas sublistas sin elemento '0' quedan: ", *filtradas, "\n")
