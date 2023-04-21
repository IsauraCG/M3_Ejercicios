#Colección desordenada de elementos. 
# Cada elemento del conjunto es único (no hay duplicados), y debe ser inmutable (no puede ser modificado). 
# Sin embargo, un conjunto es mutable, pues podemos añadir o eliminar elementos de él.

#Un conjunto se crea colocando todos los elementos dentro de llaves { }, separados por comas, o
#utilizando la función incorporada set().

#imprime todos porque no hay duplicados
es_set = set({1,2,3,4,5,6,7,8,9,0})
print(set)

#imprime sin duplicados
no_set = set({1,2,3,3,3,3,3,4,5,5,5,6,8,9,0,0,0})
print(no_set)

#añade un elemento
es_set.add(10)
print(es_set)

#Los conjuntos también pueden utilizarse para realizar operaciones matemáticas con ellos, como la
#unión, la intersección, la diferencia simétrica, entre otros

#Podemos añadir un solo elemento utilizando el método add(), y múltiples elementos utilizando el método update(). 
#El método update() puede tomar como argumento tuplas, listas, cadenas, u otros conjuntos. En todos los casos, se evitan los duplicados.

#añadir varios elementos
es_set.update({12,15,30})
print(es_set)
