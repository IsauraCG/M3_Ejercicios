""" OPERADORES DE COMPARACIÓN 

Se utilizan para comparar valores. Devuelve True o False, según la condición. 
• Operador mayor que ( > ), regresa true si el valor de la izquierda es mayor que el de la derecha. 
• Operador menor que ( < ), regresa true si el valor de la izquierda es menor que el de la derecha. 
• Operador igual que ( == ), regresa true si el valor de la izquierda es igual que el de la derecha. 
• Operador no es igual que ( != ), regresa true si el valor de la izquierda es diferente al de la derecha. 
• Operador mayor o igual que ( >= ), regresa true si el valor de la izquierda es mayor o igual que el de la derecha. 
• Operador menor o igual que ( <= ), regresa true si el valor de la izquierda es menor o igual que el de la derecha. """

x = 10 
y = 12

print('x > y es',x>y) # -> FALSE
print('x < y es',x<y) # -> TRUE
print('x == y es',x==y) # -> FALSE
print('x != y es',x!=y) # -> TRUE
print('x >= y es',x>=y) # -> FALSE
print('x <= y es',x<=y) # -> TRUE

""" COMPARACIONES 
ENTRE TIPOS La función type() devuelve el tipo del objeto, o un nuevo objeto de tipo basado en los argumentos pasados. """
print(type(x))