""" Se requiere contar con un programa que, dados 3 números diferentes, los evalúe y entregue el
orden de mayor a menor. """

N = 1234
M = 34
P = 556

list_num = [N, M, P]

if N > M and N > P:
    print(f"El número {N} es mayor que {M} y {P}")
elif M > N and M > P:
    print(f"El número {M} es mayor que {N} y {P}")
else:
    print(f"El número {P} es mayor que {N} y {M}")

list_num.sort(reverse=True)
print(f"Y el orden descendente es: {list_num}")
