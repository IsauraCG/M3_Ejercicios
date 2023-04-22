""" Un tipo de conversión implícita es el caso en que tenemos 2 variables, una de tipo entero llamada “a”, 
y otra de tipo flotante llamada “b”. Si las sumamos, y asignamos el resultado a la variable “a”, 
ésta automáticamente cambiará su tipo a flotante para poder hacer la operación. """

a = 1 
b = 2.14 
a = a + b 
print(type(a)) #Resultado: <class ‘float’>