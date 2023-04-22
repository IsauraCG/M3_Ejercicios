""" En este ejercicio sumaremos los números enteros del 1 al 10. Para resolverlo usaremos el ciclo while,
un contador al cual llamaremos i, y una variable que contendrá el resultado de la suma a la que
llamaremos suma.

Como necesitamos sumar los números del 1 al 10, el contador lo inicializaremos con el valor 1.
Luego, en cada ciclo le sumaremos una unidad. El ciclo se detendrá una vez el valor de i sea superior
a 10. Es decir que el while continuará mientras el contador i sea menor o igual a 10."""

#Inicializamos las variables i y suma
suma = 0
i = 1

#sentenciamos que while i sea menor o igual a 0 ...
while i <= 10:
    suma = suma + i         # suma va sumando el iterador al valor de var 'suma'
    i = i+1                 # actualizar contador
print("La suma es", suma)   #imprime 'La suma es' y el valor de la suma obtenida tras todos los pasos del ciclo


#Resultado: La suma es 55