""" 
La resistencia dentro de un circuito paralelo se calcula como:

RT= 1/((1 /R1)+(1/R2)+(1/R3)+(1/Rn))

Donde:

● RT es la resistencia total.
● R1 es la resistencia 1.
● R2 es la resistencia 2.
● R3 es la resistencia 3.
● Rn la n-ésima resistencia.


Realizar el código en Python para calcular la resistencia total del circuito. 
"""

# Validar que los valores ingresados para ls resistencias, sean positivos , osea mayores que cero.
# Ciclo while y funciones


def validate_input_float(texto):
    # ingreso de valores
    while True:
        try:
            # float(), str(), int() casteo o transformacion, conversion del tipo de dato
            r = float(input(texto))
            if r > 0:
                # abs(r)
                return r
            else:
                print("La resistencia ingresada es menor que '0' ")
        except Exception as error:
            print("Ha ocurrido un error en el ingreso de la resistencia ", error)
            print("Ha ocurrido un error, ingrese de nuevo el valor de la resistencia")


r1 = validate_input_float("Ingrese la resistencia 1: ")
# llamada a funcion o invocando
r2 = validate_input_float("Ingrese la resistencia 2: ")
r3 = validate_input_float("Ingrese la resistencia 3: ")
# calcular la resistencia total

rt = 1/((1/r1) + (1/r2) + (1/r3))
# imprimir la resistencia total en consola
print("La resistencia total es de", rt)


# Pedir cuantas resistencias se quieren ingresar para calcular resistencia total
# Usar un ciclo while para solicitar y verificar las resistencias x cantidad de veces
# Acumular los valores que se ingresen como resistencias, con un list o set
# Calcular la resistencia total e imporimirla en consola
