# Este es una colección desordenada de elementos.
# Cada elemento de un diccionario tiene una dupla clave/valor
# Los diccionarios están optimizados para recuperar valores cuando se conoce la clave
# Mientras que los valores pueden ser de cualquier tipo de datos y pueden repetirse, las claves deben
# ser de tipo inmutable (string, número o tupla, con elementos inmutables), y deben ser únicas.

estudiantes = {
    # clave:valor
    "Fulanito": 25,
    "Maria": 22,
    "Jose": 40,
    "Marta": 30
}

# Diccionario con claves tipo entero
mi_diccionario = {
    1: 'manzana',
    2: 'pelota'
}
# Diccionario con claves mixtas
mi_diccionario2 = {
    'nombre': 'Juan',
    1: [2, 4, 3]
}

# Para acceder a los datos de un diccionario se utilizan las claves. Las claves pueden usarse dentro
# de corchetes [ ], o con el método get().
mi_diccionario3 = {
    'nombre': 'Daniel',
    'edad': 26}
print(mi_diccionario3['nombre'])

# Otro ejemplo para obtener la edad:
print(mi_diccionario3.get('edad'))

# imprimir los valores de un diccionario
print(mi_diccionario.values())

# y cómo sería obtener el key de un value determinado.
dict_animales = {'a1': 'gato', 'a2': 'perro', 'a3': 'tigre'}
print(dict_animales['a1'])
# se genera una lista con los valores del diccionario
buscado = ""  # se define variable string que almacena el valor buscado
lista_animales = []  # se declara una 'lista_animales' que contendrá valores del diccionario
i = 0  # se declara iterador de ciclo
for key in dict_animales:  # ciclo for que recorre el diccionario y agrega a la nueva lista_animales, los values
    lista_animales.append(dict_animales[key])
    i += 1
# se indexa búsqueda en la lista_animales, en busca del valor (value) solicitado ('gato')
# se asigna el resultado de esta búsqueda a variable 'buscado'
buscado = lista_animales.index('gato')
print(f"El ítem buscado 'gato', está en el índice: {buscado}")


# OTRA FORMA DE ENCONTRAR EL VALUE EN UN DICCIONARIO
diccionario = {'a': 1, 'b': 2, 'c': 3}
valor_buscado = 2

if valor_buscado in diccionario.values():
    print("El valor buscado se encuentra en el diccionario")
else:
    print("El valor buscado no se encuentra en el diccionario")

# CORCHETE
# Al igual que en las listas y tuplas, podemos acceder a los datos anidados de los diccionarios
# usando el operador corchete.
# Primero indicaremos el índice del diccionario, y luego a los del tipo de
# estructura que corresponda.

mi_diccionario = {'Dict1': {1: 'Test'}, 'Dict2': {2: 'Prueba'}}

print(mi_diccionario['Dict1'])
print(mi_diccionario['Dict1'][1])
print(mi_diccionario['Dict2'][2])
# Resultados:
# {1: 'Test'}
# Test
# Prueba
