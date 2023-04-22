""" En el siguiente ejercicio requerimos comprobar más de una condición, y todas deben cumplirse
para la ejecución de una orden. 

Para ello haremos uso de la sentencia if y el operador and.

Realicemos el estudio de tres variables, que tendrán los valores 3, 7 y -4, respectivamente. 

En caso, de que todas sean positivas, imprimiremos un mensaje confirmándolo. 
En caso contrario, también debemos imprimir un mensaje indicándolo."""

#Primero declaramos las variables, y les asignamos sus valores respectivos 

var1 = 3
var2 = 7
var3 = -4

# A continuación, comprobamos que todas las variables sean positivas. 
# Escribiremos la sentencia if, y comprobaremos que la var1 sea mayor a cero, 
# usaremos el operador 'and' indicando que se debe cumplir también la siguiente condición, 
# que var2 sea mayor a cero. 
# De la misma forma haremos para var3. 
# Recordemos colocar los dos puntos luego de la primera línea de la sentencia 'if', y la indentación en el cuerpo.

if var1 > 0 and var2 > 0 and var3 > 0 :
    print("Todas las variables son positivas.")

# Finalmente, debemos indicar qué sucederá en caso de que no todas sean positivas con la 
# sentencia else. Recordar los dos puntos de la sintaxis, y el uso de la indentación.

else :
    print("No todas las variables son positivas")