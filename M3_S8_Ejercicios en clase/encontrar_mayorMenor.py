# Tienes la siguiente lista de números:

lista_nums = [45, 23, 67, 89, 12, 56, 78, 90]

# Encontrar el número más grande en la lista utilizando un bucle for.

maximo = lista_nums[0]

for num in lista_nums:
    if num > maximo:
        maximo = num

print(f"El número mayor es {maximo}")


# Encontrar el Mayor y el Menor

lista = [45, 23, 67, 89, 12, 56, 78, 90, 45, 67, 12]
mayor = lista[0]  # lista[-1] parte desde el final
menor = lista[0]
# mayor = menor = lista[0] # declaracion de multiples variables de mismo valor

for num in lista:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(
    f"El elemento de mayor valor es: {mayor}\nY el elemento de menor valor es: {menor}")
