password = "confidencial123"
solicitud_clave = input("Ingrese su clave ")

while password != solicitud_clave:

    print("error, no coincide su clave")

    solicitud_clave = input("Ingrese su clave ")

print("Bienvenido!")
