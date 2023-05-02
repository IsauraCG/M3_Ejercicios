
# lista con 7 elementos

# índice [0, 1, 2, 3, 4, 5]
lista = [1, 2, 3, 4, 5, 6, 1]

# recorriendo los elementos de la lista
for item in lista:
    print(f"Un elemento de la lista es: {item}")

print("\n")

# range (start, stop , iteration), estipula un rango apra recorrer según indices
# es decir, start = valor de inicio / stop = valor de tope / iteration = de uno en uno, de dos en dos

# Recorriendo el índice de la lista con range
print("Recorriendo la lista:")
for item in range(len(lista)):
    print(
        f"Índice [{item}]  :  Elemento ({lista[item]})")

print("\n")

# Para el caso en que se solicita encontrar un elemento en la lista
# o ver cuántas veces está repertido el item en la lista

# se establece variable contador que irá acumulando las veces que encuentra el elemento por vuelta del ciclo
contador = 0
print("Recorriendo la lista, buscando el elemento '1' duplicado, y cuántas veces aparece: ")
for item in lista:
    print("Recorriendo el elemento de la lista ", item)
    if item == 1:  # cada vez que encuentra coincidencia de elemento '1'
        contador += 1  # suma una vez al contador y lo acumula
        # imprime este mensaje cada vez que encuentra un elemento '1'
        print("\t\t Item encontrado!")

    # imprime el valor del contador, con als veces que se repite el elemnto
print(f"El número '1' ha aparecido {contador} veces\n")

# recorriendo o conociendo el indice de la lista
for item in lista:
    print(f"Recorriendo y mostrando, índice: {lista.index(item)}")


# SI QUIERES VERIFICAR SI UN ELEMENTO ESTÁ EN UNA LISTA,
# NO SE USA SIEMPRE FOR: PUEDES USAR 'IN' O 'NOT IN' .s
claves = ['456', '654', '156', '345', '234', '890']

clave_ingresada = input("Por favor ingrese su clave numérica de 3 dígitos: ")
condicion = True

while True:
    if clave_ingresada in claves:
        print("Bienvenido/a a Tachibank")
        condicion = False
        break
    elif clave_ingresada not in claves:
        # print("Buscando ...")
        print("La clave no existe")
        clave_ingresada = input(
            "Por favor ingrese su clave numérica de 3 dígitos: ")
