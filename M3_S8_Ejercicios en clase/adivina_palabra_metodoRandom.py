# Adivinar una palabra random predeterminada

# Importar librería random
import random

# Declaro lista de palabras existentes
palabras_secretas = ["arroz", "pollo", "pure", "choclo", "seitan"]

# Declaro la variable que almacena la opción secreta que el método random.choice escoge
adivinar = random.choice(palabras_secretas)

# print(adivinar)

intentos = 5
turno = 0
ingreso = ""

while adivinar != ingreso and turno < intentos:
    ingreso = input("ingrese la palabra: ")
    turno += 1

    if ingreso == adivinar:
        print(f"ha encontrado la palabra secreta en {turno} turno ")
    elif turno == intentos:
        print(f"no tiene mas intentos, la palabra secreta era: {adivinar}")
    else:
        print(f"sigue intentando, vas en el turno {turno}")
