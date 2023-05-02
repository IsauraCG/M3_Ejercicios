while True:
    try:
        number = int(input("Ingrese un número: "))
        if number > 1:
            print("El número es mayor a 1")
        else:
            print("El número es menor o igual a 1")
            break
    except ValueError:
        print("Por favor, ingrese un número válido.")

# .
