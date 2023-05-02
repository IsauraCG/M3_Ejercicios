# Importa librería random, para que saque al azar una palabra de una lista
import random

# Declaración de lista que contiene los elementos o 'palabras' a escoger por metodo random
personas = ["Natalia", "Joaquin", "Onofrio", "Adrian", "Victor", "Eduardo", "Federico",
            "Aaron", "Ignacio", "Camilo"]

# Declaración de variable 'palabra' que contiene el elemnto escogido por random, y en minúsculas
palabra = random.choice(personas).lower()

# lista que almacena todos los valores 'letra' ingresados por el usuario en cada intento.
adivinado = []

# Lista que almacena los valores 'letra' acertados
match = []

# vidas = 6

# Función para mostrar el estado actual del juego


def mostrar_estado(adivinado, palabra):
    # Muestra el estado actual del juego, con las letras adivinadas
    # y las letras que faltan por adivinar
    for letra in palabra:  # For loop que recorre cada caracter en 'palabra' e identifica si la 'letra' está en ella
        if letra in adivinado:  # Si 'letra' está en 'palabra' ...
            print(letra, end=" ")  # Imprime la 'letra' y un espacio al final
        else:  # Sino, imprime '_' y un espacio al final
            print("_", end=" ")
    print("\n")


# Bienvenida
print("Adivina la palabra secreta.")

# declara variable 'respuesta' que almacena las letras que ingresa el usuario
# Solicita ingresar una letra
respuesta = input("Ingresa una letra: ")

# Mientras que el largo de 'palabra' sea distinto del largo de 'adivinado'
# (que es lo formado por las letras ingresadas), se solicita ingresar una letra
while len(match) != len(palabra):
    # Verifica y condiciona la respuesta recibida
    if len(respuesta) > 1:  # Si ingresa más de un caracter, solicita ingresaar 1 letra
        print("Ingresa solo 1 letra")
        respuesta = input("Ingresa una letra: ")
    elif len(respuesta) == 0:  # Si no ingresa nada, solicita ingresar al menos 1 letra
        print("Por favor ingresa algo.")
        respuesta = input("Ingresa una letra: ")
    else:  # Si ha ingresado sólo 1 letra, la añade a la lista de 'adivinado'
        mostrar_estado(adivinado, palabra)
        adivinado.append(respuesta)
        print(match, adivinado)
    respuesta = input("Ingresa una letra: ")


"""         elif len(palabra) == len(adivinado):
            print("¡¡FELICIDADES!!\n Haz ganado")
            break """
