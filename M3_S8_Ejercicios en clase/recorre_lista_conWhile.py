# Tenemos una lista de números

lista = [3, 5, 2, 8, 1, 10]

# Se requiere encontrar el primer número par en la lista utilizando un bucle while.

i = 0

while i < len(lista):
    if lista[i] % 2 == 0:
        print(f"El primer numero par es {lista[i]}")
        break
    i += 1
else:
    print("No hay numeros pares")
