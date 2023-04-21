#scope o alcance de una variable

#alcance global
#alcance local

#variable de alcance global porque no esta dentro de alguna estructura
#Se pueden acceder, llamar y reasignar en todo el documento
variable_global = "se puede acceder desde todo el documento"


#metodo o funcion para ejemplicar una variable local
#def nombre_metodo(parametros_entrada):
def suma(a,b):
    suma_valores = a+b #variable local porque existe solo dentro de la estructura de la funcion o metodo
    #variable_global = suma_valores #asignando suma a la variable global
    if True:
        print(suma_valores)
    return suma_valores

print(suma(2,1)) #3
operacion = suma(7,2)
print(variable_global)
# print(suma_valores)   
# #NameError: name 'suma_valores' is not defined --> esto es porque es local y no se puede imprimir desde fuera
