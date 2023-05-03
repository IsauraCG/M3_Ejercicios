# Coleccion de elementos inalterados, la idea es no eliminar elementos, aunque se puede
# Si hay que modificar elementos, mejor usar listas
# El índice -1 se refiere al último elemento, -2 al penúltimo elemento, y así sucesivamente.


tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# Una tupla puede tener cualquier número de elementos, y éstos pueden ser de diferentes tipos
# (entero, flotante, lista, cadena, entre otros).
# tupla con tipos de datos mixtos
mi_tupla = (1, "Hola", 3.4, 0.56, "gato")
print(mi_tupla)

# Para acceder se usa : nomre_tupla[indice]
asignar_tupla = tupla[2]
print(tupla[2])
print(mi_tupla[3])

# o almacenado en variable
elemento_tupla = tupla[3]
print(elemento_tupla)

# INDEXACIÓN
# En el caso de que tengamos listas o tuplas anidadas, podemos acceder a los valores internos
# haciendo uso de cada uno de los índices, indicando primero el índice externo, luego el índice del
# siguiente nivel, y así sucesivamente.

mi_lista = [[1, 2, 3], [4, 5]]

print(mi_lista[0])
print(mi_lista[0][1])
# Resultado:
# [1, 2, 3]
# 2 .
