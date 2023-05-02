""" # Recorrer los datos numéricos que se encuentran dentro de la siguiente lista de listas: """
import time
lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
# Se debe imprimir cada dato de las listas en pantalla con las siguientes excepciones:
#   • Si el primer número de la sublista es cero, omitir la impresión de toda la sublista.
#   • Si existe un cero en cualquier otra posición, omitir solo la impresión del cero.

for sbl in lista:
    if sbl[0] == 0:  # si subista empieza en 0 sáltala
        continue

    for num in sbl:  # recorre sublista 'subl'
        if num == 0:  # si num es '0'
            continue
        print(num)    # sino imprime num
        time.sleep(0.5)  # temporizador para mostrarlo pausadamente
