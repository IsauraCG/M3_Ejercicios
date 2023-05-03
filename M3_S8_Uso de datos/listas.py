# listas en python
# estructura para almacenar datos con un orden especifico de inseccion

# Una lista de enteros
mi_lista = [1, 2, 3]

lista = [1, 2, 3, 4]
boolean = False
lista_compleja = [1, "2", 3, (1+3), 1.5, lista, boolean]
print(lista_compleja)

# Para acceder a los valores de una rreglo, se usan los índices
# Los índices van desde 0 a n
# Los indices también pueden ser negativos, pero en este caso accede a los elementos desde el último hacia adelante

# imprinme el valor '1', que está en el índice 0 de la list 'lista'
print(lista[0])

# imprinme el valor '3', que está en el índice -2 de la list 'lista'
print(lista[-2])

# Añade elementos a la lista
lista.append(5)
print(lista)

# Remueve el primer valor coincidente en la lista
lista.remove(3)
print(lista)

# pop extrae un valor de la lista, puede indicarse el indice, y el valor se puede almacenar en otra variable
a = lista.pop(1)
print(a)
print(lista)

# inserccion por indice, en este caso inserta el numero '2' en el índice '1 de la lista
lista.insert(1, 2)
print(lista)  # imprime 1,2,4,5.

# indice por elemento
indice = lista.index(2)
print(indice)  # imprime el elemento en el indice (2)
