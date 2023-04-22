""" En este ejemplo utilizaremos la sentencia for para recorrer una lista de números y sumarlos. 
Para ello, primero creamos la lista de números con los números: 6, 5, 3, 8, 4, 2, 5, 4 y 11.  """

numeros = [6, 5, 3, 8, 4, 2, 5, 4, 11]
SUMA = 0
for val in numeros:
    SUMA = SUMA + val
print("La SUMA es", SUMA)
# Resultado: La SUMA es 48
