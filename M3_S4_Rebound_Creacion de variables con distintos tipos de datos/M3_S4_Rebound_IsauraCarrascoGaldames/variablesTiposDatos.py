""" Requerimos crear una variable con el número 8, una con el número 10.5, y una con la palabra “ejercicio”. 
Luego, crear un set que contendrá cada una de las variables que creamos, y será asignado a una variable.
A continuación, crearemos una lista que contendrá el set creado anteriormente, y una variable con
el valor lógico False. Esta lista la asignaremos a una variable que luego imprimiremos en pantalla """

#Crear una variable con el número 8
var_ocho = 8

#Crear una con el número 10.5
var_float = 10.5

#Crear una con la palabra “ejercicio”
var_string = "ejercicio"

#Crear un set que contendrá cada una de las variables que creamos, y será asignado a una variable
var_set = set({var_ocho,var_float,var_string})

#Crear una lista que contendrá el set creado anteriormente, y una variable con el valor lógico False
#Esta lista la asignaremos a una variable que luego imprimiremos en pantalla
var_boolean = False
list_required = [var_set,var_boolean]
print(f"La lista requerida es: {list_required}")