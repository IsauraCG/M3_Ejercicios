#Este es una colección desordenada de elementos. 
#Cada elemento de un diccionario tiene una dupla clave/valor
#Los diccionarios están optimizados para recuperar valores cuando se conoce la clave
#Mientras que los valores pueden ser de cualquier tipo de datos y pueden repetirse, las claves deben
#ser de tipo inmutable (string, número o tupla, con elementos inmutables), y deben ser únicas.

estudiantes = {
    #clave:valor
    "Fulanito":25,
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

#Para acceder a los datos de un diccionario se utilizan las claves. Las claves pueden usarse dentro
#de corchetes [ ], o con el método get().
mi_diccionario3 = {
    'nombre': 'Daniel', 
    'edad': 26}
print(mi_diccionario3['nombre'])

#Otro ejemplo para obtener la edad:
print(mi_diccionario3.get('edad'))