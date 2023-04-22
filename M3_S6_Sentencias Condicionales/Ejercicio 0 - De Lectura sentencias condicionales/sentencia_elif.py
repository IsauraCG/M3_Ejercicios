""" En otros lenguajes de programación tenemos la sentencia switch, 
el creador de Python consideró que elif podía cumplir con esa función de forma más sencilla. """

""" la sintaxis es la siguiente: 

if expresión a probar: 
    Instrucciones en caso de ser verdadero 
elif Segunda expresión a probar: 
    Instrucciones en caso de ser verdadero 
else: 
    Instrucciones en caso de ser falso """
    
x = 1 

if x > 10: 
    print(" x es mayor que 10!") 
elif x < 10: 
    print("x es menor que 10!") 
elif x < 20 : 
    print("x es menor que 20!") 
else: print("x es igual a 10")