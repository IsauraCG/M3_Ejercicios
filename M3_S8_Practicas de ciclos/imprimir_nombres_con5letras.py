# Se tiene la lista de nombres, imprimir los nombres con más de 5 letras
# lista = ["Juan", "María", "Pedro", "Ana", "Roberto", "Lucía", "Luisa"]

# Declarar variable que almacena lista
nombres = ["Juan", "María", "Pedro", "Ana", "Roberto", "Lucía", "Luisa"]

for nombre in nombres:
    if len(nombre) >= 5:
        print(f"{nombre}")

# si quiere imprimir cuántos nombres tienen 5 o más caracteres.
contador = 0
for nombre in nombres:
    if len(nombre) >= 5:
        contador += 1
print(f"{contador}")

# opcion rebuscada
name = ["Juan", "Maria", "Pedro", "Ana", "Roberto", "Lucia", "Luisa"]
name_len_five = list(filter(lambda x: len(x) >= 5, name))
print(name_len_five)
