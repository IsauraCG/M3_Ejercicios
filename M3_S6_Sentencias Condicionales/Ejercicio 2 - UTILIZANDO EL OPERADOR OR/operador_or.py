""" Realicemos el estudio de tres variables, que tendrán los valores -3, 7 y -4, respectivamente. En caso
de que alguna sea positiva, imprimiremos un mensaje confirmándolo. En caso contrario, también
debemos imprimir un mensaje indicándolo. """

# Primero declaramos las variables, y les asignamos sus valores respectivos.
var1 = -3
var2 = 7
var3 = -4

""" A continuación, comprobamos que alguna de las variables sea positiva. Para ello escribiremos la
sentencia if, y comprobaremos que la var1 sea mayor a cero, usaremos el operador or indicando
que si la comparación anterior es falsa podemos estudiar la siguiente y chequear si es verdadera,
es decir que var2 sea mayor a cero. De la misma forma haremos para var3. Recordemos colocar
los dos puntos luego de la primera línea de la sentencia if, y la indentación en el cuerpo. """

if var1 > 0 or var2 > 0 or var3 > 0 :
    print("Alguna de las variables es positiva.")
else : #Finalmente, debemos indicar qué sucederá en caso de que ninguna de las variables
    print("Ninguna de las variables son positivas ")

# Resultado: TRUE, por tanto coloca: "Alguna de las variables es positiva."