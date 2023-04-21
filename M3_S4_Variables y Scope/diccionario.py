#Conjunto de datos que van indexionados y ordenados según clave y valor
#Declaracion con llaves o con dict()
# clave : valor

estudiantes = {
    #clave:valor
    "Fulanito":25,
    "Maria": 22,
    "Jose": 40,
    "Marta": 30
}

print(estudiantes) #{'Fulanito': 25, 'Maria': 22, 'Jose': 40, 'Marta': 30}

#acceder al valor de una clave
# diccionario["Fulanito"]

print(estudiantes["Fulanito"]) #25

#get()
#Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto:
print(estudiantes.get)
