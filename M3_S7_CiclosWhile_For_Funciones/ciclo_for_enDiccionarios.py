"""
diccionario
"""
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# obteniendo el valor de una key
print("Obteniendo los 'key' de cada elemento en 'diccionario': ")
for item in diccionario:
    print(item)  # a b c d e f

# obteniendo el value de una clave
print("Obteniendo los 'value' de cada elemento en 'diccionario': ")
for item in diccionario:
    print(diccionario[item])  # 1 2 3 4 5 6

# obteniendo solo los valores
print("Obteniendo el 'value' de cada elemento en 'diccionario': ")
for i in diccionario.values():
    print(i)  # 1 2 3 4 5 6

# obteniendo solo los keys o clave
print("Obteniendo cada elemento con formato key:value")
for temp in diccionario.items():
    print(temp)  # clave:valor ('a', 1) ...
