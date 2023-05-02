# Aunque recorrer datos es mejor con un For, pero, existe while.

# Pensar cual es la condicion para que el ciclo quiebre y termine

i = 0

while i < 5:  # ciclo que se ejecuta siempre que 'i' sea menor que 5
    i += 1
    print(i)

j = 1  # ciclo que se ejecuta siempre que 'j' sea menor o igual a 5
while j <= 5:
    print(j)  # 1


j += 1  # aumentando el valor de i como iterador
while True:
    print("Imprime hasta que")
    break  # terminar el ciclo con break
