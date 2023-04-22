""" Podemos tener una sentencia if...elif...else dentro de otra sentencia if...elif...else. 
Esto se llama anidación en la programación informática.
Cualquier número de estas sentencias puede estar anidado dentro de otro. 
La indentación es la única manera de averiguar el nivel de anidamiento. 
Pueden resultar confusas, por lo que deben evitarse a menos que sea necesario. """

num = 4 
if num >= 0 :
    
    if num == 0: 
        print("Cero") 
    else: 
        print("Número positivo") 
        
else: print("Número negativo")