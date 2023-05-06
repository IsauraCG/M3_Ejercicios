""" 
La resistencia dentro de un circuito paralelo se calcula como:

RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))

Donde:

● RT es la resistencia total.
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.


Realizar el código en Python para calcular la resistencia total del circuito. 
"""

# Declaracion de variables, solicitando los valores a evaluar
r1 = float(input("Por favor ingrese un valor para resistncia 1 : "))
r2 = float(input("Por favor ingrese un valor para resistncia 2 : "))
r3 = float(input("Por favor ingrese un valor para resistncia 3 : "))

# aplicando variables a la fórmula de cálculo
rt = 1/((1 / r1)+(1/r2)+(1/r3))

# imprimiendo valores, con formato de max 3 decimales *PD: l valor se aproxima*
print("La resistencia total es: {:.3f}".format(rt))
