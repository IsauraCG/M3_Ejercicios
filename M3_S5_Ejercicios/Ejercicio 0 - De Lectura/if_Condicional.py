""" Nótese que es importante la indentación, todas las instrucciones en caso de ser verdadero deben tener 
una indentación de al menos 4 espacios en blanco con respecto a la expresión if. 

else (en caso contrario): esta sentencia siempre se usa para indicar qué debe suceder en caso de que la sentencia if sea falsa, 
siempre y cuando no existan más condiciones posibles. 

Es decir, solo tenemos 2 opciones. La sintaxis es como sigue: 
"""
#if expresión a probar: 
#    Instrucciones en caso de ser verdadero 
#else: 
#    Instrucciones en caso de ser falso

'''En este programa, comprobamos si el número es positivo o negativo o cero, y mostrar un mensaje apropiado'''
num = 3.4 
if num > 0: 
    print("Número positivo") 
elif num == 0 : 
    print("Cero") 
else : print("Número negativo")   


