"""
Listas, colecciones de datos
Son llamadas tambien arreglos
Se definen por [] corchetes
Se definen utilizando la funcion list()
"""
# indices desde 0 a n-1, siendo n la cantidad de elementos
# indices[0, 1, 2, 3, 4, 5]
lista = [1, 2, 3, 4, 5, 6]  # definiendo una lista con valores 1, 2, 3, 4, 5, 6
otra_lista = []  # definiendo una lista vacia
otra_lista = list()  # definiendo una lista vacia
otra_lista = [31, 1.72, "Fulanito", "Perez"]  # definiendo una lista vacia

# acceder a la longitud o largo de la lista con funcion len()
print("Longitud de lista, ", len(lista))
print("Longitud de otra_lista, ", len(otra_lista))

# conocer el tipo de dato
print("El tipo de dato de lista es: ", type(lista))  # <class 'list'>

# acceder a los elementos de la lista a traves de su indice
# indices positivos van desde la primera parte de la lista
print("Elemento en el indice 0 de la lista: ", lista[0])
# indices negativos van desde la ultima parte de la lista
print("Elemento en el indice -1 de la lista: ", lista[-1])

# contar los elementos existentes de la lista con la funcion count() dado un elemento a contar, ej nombre_lista.count(elemento_a_contar)
print("Cantidad de veces que se repite el 1 en la lista: ", lista.count(1))

# acceder al indice de un elemento de la 'otra_lista' con la funcion index().
print("Indice del elemento Fulanito en la otra_lista: ",
      otra_lista.index("Fulanito"))

# desempaquetar elementos de la lista en variables.
print("\nDesempaquetar")
edad, altura, nombre, apellido = otra_lista
print("Edad: ", edad)
print("Altura: ", altura)
print("Nombre: ", nombre)
print("Apellido: ", apellido)
print(otra_lista, "\n")

# crear, insertar, actualizar y eliminar elementos de la lista
# crear un nuevo elemento en la lista con funcion append(), añadir
lista.append(7)  # [1,2,3,4,5,6,7]
print("La lista es: ", lista)

# insertar elemento en la lista con funcion insert(index,elemento_insertar)
lista.insert(6, 8)
print("La lista es: ", lista)  # [1, 2, 3, 4, 5, 6, 8, 7]

# actualizar elemento en la lista, nombre_lista[indice_actualizar] = valor_asignar
lista[6] = 7
lista[7] = 8
# lista[7] = "Arroz"
print("La lista es: ", lista)  # [1, 2, 3, 4, 5, 6, 7, 8]

# remover el elemento
#   ojo que no se deben agregar strings en listas numericas int
#   por ello, volvemos a  string los int de la lista antes de agregar 'Arroz'
#   y los vamos acumulando en una nueva lista 'lista_string'
lista_string = []
for num in lista:
    lista_string.append(str(num))

# se agrega primero el elemento
lista_string.append("Arroz")
print("La lista es: ", lista_string)
# se remueve el elemento
lista_string.remove("Arroz")
print("La lista es: ", lista_string)

# algunas funciones de la lista
# count(), len(), index(), insert(), remove(), pop(), sort(), reverse()

# funcion pop(indice) extrae un elemento dado un indice por default extrae el ultimo elemento de la lista con indice -1
lista.append(9)
print("La lista es: ", lista)
elemento_extraido = lista.pop(8)
print("La lista es: ", lista)

# funcion sort() ordena los elementos de la lista, reverse=True reverse=False
# otra_lista.sort() #[31,1.72,"Fulanito","Perez"] no permite ordenar listas con varios elementos de diferente tipo
lista.sort(reverse=True)
print("La lista es: ", lista)  # [8, 7, 6, 5, 4, 3, 2, 1]
# lista.sort() por defecto toma reverse=False y ordena los elementos de menor a mayor

# funcion reverse() los ultimos elementos cambian a ser primero y los primero cambian a ser último
lista.reverse()
print("La lista es: ", lista)

# INDEXACIÓN
# En el caso de que tengamos listas o tuplas anidadas, podemos acceder a los valores internos
# haciendo uso de cada uno de los índices, indicando primero el índice externo, luego el índice del
# siguiente nivel, y así sucesivamente.

mi_lista = [[1, 2, 3], [4, 5]]

# imprime el elemento en el índice [0] de la lista. (que en este caso es lista [1,2,3])
print(mi_lista[0])
# imprime el elemento en indice [1] de ña sublista, del elemento índice [0] en la lista '2'
print(mi_lista[0][1])
# Resultado:
# [1, 2, 3]
# 2
