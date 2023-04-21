""" En este ejercicio requerimos ejecutar un ciclo, el cual saltará una iteración si se cumple una condición
preestablecida. Para ello utilizaremos la sentencia continue.
Debemos imprimir en pantalla las letras de la palabra cadena, exceptuando las apariciones de la letra
“a”. Luego, imprimiremos la palabra fin. """

for val in "cadena":
    if val == "a":
        continue
    print(val)
print("Final")