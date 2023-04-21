""" Ahora requerimos imprimir todos los números contenidos en una lista, y cuando la hayamos
recorrido toda debemos imprimir un mensaje que indique que no quedan más elementos en la
misma. 

Para resolver este problema, primero recorreremos la lista haciendo uso de una instrucción for, y
luego utilizaremos la sentencia else que indicará que ya recorrimos toda la lista para imprimir el
mensaje solicitado."""

digitos = [0, 1, 5] #lista

for i in digitos:   #para la variable i en lista digitos
    print(i)        #imprime el valor de 'i'
else:               #sino
    print("No quedan elementos en la lista.") #imprime el mensaje cuando 'i' o enteros ya no existen en la lista digitos


#Resultado: No quedan elementos en la lista.
