# Encontrar constraseña ingresada con una de lista predefinida

# Declara
claves = ['456', '654', '156', '345', '234', '890']

clave_ingresada = ""
condicion = True

clave_ingresada = input(
    "Por favor ingrese su clave numérica de 3 dígitos: ")

while True:
    if int(len(clave_ingresada)) == 3:
        if clave_ingresada in claves:
            print("Bienvenido/a a Tachibank")
            condicion = False
            break
        elif clave_ingresada not in claves:
            # print("Buscando ...")
            print("La clave no existe")
            clave_ingresada = input(
                "Por favor ingrese su clave numérica de 3 dígitos: ")

    elif int(len(clave_ingresada)) > 3:
        print("Debe ingresar una clave numérica de 3 dígitos")
        clave_ingresada = input("Por favor ingrese su clave: ")

    elif clave_ingresada == " " or int(len(clave_ingresada)) == 0:
        print("No ha ingresado nada.\nPor favor ingrese una clave.")
        clave_ingresada = input(
            "Por favor ingrese su clave numérica de 3 dígitos: ")
    else:
        print("ERROR, vuelva recargar el sitio.")
        break
