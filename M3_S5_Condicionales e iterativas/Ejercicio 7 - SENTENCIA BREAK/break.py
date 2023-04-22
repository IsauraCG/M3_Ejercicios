""" En este ejercicio vamos a detener la ejecución de un ciclo cuando una condición se cumpla. Para ello
haremos uso de la sentencia break.
Imprimiremos en pantalla las letras de la palabra murciélago, sin embargo, detendremos la ejecución
del ciclo cuando encontremos una letra c. Luego, imprimiremos la palabra fin. """

for val in "murcielago":
    if val == "c":
        break
    print(val)
print("Fin")

#Resultado: m  u  r  Fin
