""" 
Realizar el calculo de la hipotenusa requiriendo el ingreso del cateto a y cateto b 
por parte del usuario en consola
"""

import math

A = float(input("Por favor, un vaor para cateto A:"))
B = float(input("Por favor, un vaor para cateto B:"))
hipotenusa = (math.sqrt((A*A)+(B*B)))
print(f"la hipotenusa es {hipotenusa}")

# otro formato
print("La hipotenusa total es: {:.2f}".format(hipotenusa))
