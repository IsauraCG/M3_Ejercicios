"""Realizar la ejecución de un menú utilizando el lenguaje 
Python, donde se le indiquen varias opciones a seleccionar 
por el usuario y una opción para salir del menú.
Utilizar ciclos y estructuras condicionales."""

while True:

    opcion = input("Hola, bienvenido\n"
                   "1.- Saludar\n"
                   "2.- Preguntar qué programación hay disponible\n"
                   "3.- Operar con dos valores\n"
                   "4.- Preguntar cómo estará el clima\n"
                   "5.- Salir\n\n"
                   "Ingresa una opción : ")

    match opcion:
        case "1":
            print("Hola, te estoy saludando\n\n")
        case "2":
            print(
                "Las series disponibles son:\n - La Ley y el Orden\n - Viaje a las Estrellas\n - The Office\n")
        case "3":

            opcOperar = input("Por favor ingresa qué quieres hacer: \n"
                              " 1 - Sumar\n"
                              " 2 - Restar\n"
                              " 3 - Multiplicar\n"
                              " 4 - Dividir\n\n"
                              "Ingresa tu opción: ")
            match opcOperar:
                case "1":
                    A = int(input("Por favor, numero: "))
                    B = int(input("Ingreso otro numero: "))
                    suma = A + B
                    print(f"El resultado de la operación es: {suma}\n")

                case "2":
                    A = int(input("Por favor, numero: "))
                    B = int(input("Ingreso otro numero: "))
                    resta = A - B
                    print(f"El resultado de la operación es: {resta}\n")
                case "3":
                    A = int(input("Por favor, numero: "))
                    B = int(input("Ingreso otro numero: "))
                    producto = A * B
                    print(f"El resultado de la operación es: {producto}\n")
                case "4":
                    A = int(input("Por favor, numero: "))
                    B = int(input("Ingreso otro numero: "))
                    cuociente = A / B
                    print(
                        f"El resultado de la operación es: {cuociente:.2f}\n")

        case "4":
            print("Estará lluvioso\n\n")
        case "5":
            print("Nos vemos!")
            break
        case _: print("Esa opcion no es válida!")
