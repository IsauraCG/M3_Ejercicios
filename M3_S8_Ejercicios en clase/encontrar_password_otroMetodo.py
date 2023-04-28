password = "confidencial123"
solicitud_clave = input("Ingrese su clave ")

oportunidades = 0
while password != solicitud_clave and oportunidades < 3:

    print("error, no coincide su clave")

    oportunidades += 1
    solicitud_clave = input(
        f"Le quedan {3 - oportunidades} intentos. Ingrese su clave ")

if oportunidades == 3:

    print("Se bloquea el ingreso")

elif password == solicitud_clave:

    print("Bienvenido")
