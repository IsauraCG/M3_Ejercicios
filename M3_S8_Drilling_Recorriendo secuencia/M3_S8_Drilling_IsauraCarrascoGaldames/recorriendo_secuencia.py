# Se solicita recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas:
import pprint
listas = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

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
""" Imprimir cada dato de la lista con sublistas en pantalla, con excepciones """
# Se declara un diccionario a la que después se asignarán los valores y claves según el requerimiento
diccionario = dict()
# declaracion de variable que almacena las listas ya filtradas y las denomina "filtradas" del diccionario
filtradas = []
# variabe iterador
i = 0
# se declara una lista para contener los valores de las claves indicadas en requerimientos
keys = ['A', 'B', 'C', 'D']

# se establece ciclo for que realiza el filtro de los valores o números que cumplen con los requerimientos
for lista in listas:
    if lista[0] == 0:  # condiciona si la sublista empieza con '0' ejecute:
        # variable que contine valor del indice de la sublista
        indice_remover = listas.index(lista)
        # remueve el índice capturado anteriormente de la lista 'keys'
        keys.remove(keys[indice_remover])
        # continue, para que no muestre la sublista
        continue
    else:  # cuando condición anterior nose cumple (sublista no empieza en '0')
        filtradas.append(lista)  # añade la sublista a la lista de 'filtradas'
        for num in lista:  # ciclo for que recorre los numeros de la sublista
            if num == 0:  # condiciona que si el número de sublista es '0' ejecute:
                lista.remove(num)  # remover número de la lista

# imprime el listado de sublistas 'filtradas'
print("\nLas sublistas y sus valores filtrados son: ", filtradas)

# Se crea diccionario, asignando a cada 'key' su respectivo value sacado de la nueva lista 'filtradas'
diccionario = dict(zip(keys, filtradas))
# imprime dicccionario resultante

print("\nEl diccionario resultante queda: ")
pprint.pprint(diccionario)
print("\n")
