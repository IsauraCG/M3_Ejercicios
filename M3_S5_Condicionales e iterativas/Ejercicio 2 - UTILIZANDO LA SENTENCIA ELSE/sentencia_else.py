""" Ahora escribamos un programa que chequee si el número es mayor o igual a cero; o si por el
contrario, es negativo, emitir un mensaje en pantalla según sea el caso """

num = 3
if num >= 0:
    print(num, "es positivo o cero")
    #Luego, debemos escribir qué sucederá en caso de que la comparación anterior sea falsa; es decir,
    #que el número es menor a cero = negativo. Para ello utilizamos la sentencia else, recordando que se
    #colocan los dos puntos luego del else, y que se respeta la indentación en el cuerpo de la instrucción de éste.
else :
    print(num, "es negativo")
