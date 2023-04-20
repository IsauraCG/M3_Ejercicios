""" EJERCICIO:
El objetivo de la presente actividad es realizar un cálculo aritmético sencillo, haciendo uso de
variables, operaciones aritméticas, y de la función print(). Para ello requerimos importar el
módulo math.

ENUNCIADO DEL PROBLEMA:
Requerimos hacer el cálculo de la raíz cuadrada de una variable llamada “y” que tiene valor 81,
utilizando el módulo de la librería math incorporada en Python. El resultado debemos asignarlo a
una variable que será impresa en pantalla 
"""
# Se importa math para poder operar
import math

# Se declara la variable 'y' otorgada por el requerimiento
y = 81

# Se declara una variable que contiene el resultado de la operación de 'la raíz cuadrada' de la variable 'y'
raizCuadrada = math.sqrt(y)

# Impresión de un mensaje y el resultado de la operación requerida
print(f"La raíz cuadrada de la variable 'y', cuyo valor es 81, es: {raizCuadrada}")