# Con lista de elementos, imprimir la longitud de cada elemento

# Declarar lista
animales = ['Gato', 'Perro', 'Tigre', 'Elefante', 'Ballena', 'León']
# Declaro lista que almacena longitudes
longitudes = []

for animal in animales:
    longitud = len(animal)
    longitudes.append(longitud)
print(longitudes)


# Otra solución
lista = ["gato", "perro", "elefante", "jirafa", "tigre"]
longitudes = []

for i in range(len(lista)):
    longitudes.append(len(lista[i]))
    print(longitudes)

for i in lista:
    longitudes.append(len(i))
    print(longitudes)
