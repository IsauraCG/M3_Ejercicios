""" Se solicita crear un diccionario en Python para almacenar los precios
de diferentes productos en una tienda en línea.
Las claves del diccionario serán los nombres de los productos 
y los valores serán los precios de los productos.
A continuación, se solicita recorrer el diccionario e imprimir los productos 
cuyos precios son superiores a 50 dólares. 
Finalmente, se debe calcular el precio total de los productos cuyos nombres 
empiezan con la letra 'C' y mostrarlo en pantalla.

precios = {
    'camisa': 30,
    'pantalon': 50,
    'zapatos': 80,
    'calcetines': 10,
    'chaqueta': 100} """

def crear_diccionario (diccionario):
    """ Función que crea un diccionario """
    key = input("Ingrese producto:")
    value = int(input("Ingrese precio: "))
    diccionario[key]=value
    # print(diccionario)
    return diccionario

def ingresar_items (diccionario):
    """ Función que pregunta si dea ingresar o no nuevos productos, si es así, 
    los agrega a diccionario entregado """
    while True:
        opcion = input("\n1 - Agregar nuevo producto"+
                       "\n2 - Imprimir listado de productos"+
                       "\n3 - Imprimir productos sobre USD$ 50"+
                       "\n4 - Imprimir precio total y productos que empiezan con 'C'"+
                       "\n5 - Salir"
                       "\nIngresa una opción: ")
        if opcion == '1':
            crear_diccionario(diccionario)
        if opcion == '2':
            print(diccionario)
        if opcion == '3':
            recorre_diccionario(diccionario)
        if opcion == '4':
            calcular_precios(diccionario)
        if opcion == '5':
            print("Hasta Pronto :)")
            break

def recorre_diccionario (diccionario):
    """ Funcion que recorre diccionario e imprime los productos 
    con precios superiores a 50 """
    diccionario_sobre50 = {}
    for key in diccionario:
        if diccionario[key] > 50:
            # print(f"{key} : {diccionario[key]}")
            diccionario_sobre50[key] = diccionario[key]
        else:
            continue
    print("Los productos sobre USD$50 son:" , diccionario_sobre50)
    return diccionario_sobre50

def calcular_precios (diccionario):
    """ Función que calcula el precio total de los productos cuyos nombres 
    empiezan con la letra 'C' y los muestra en pantalla """
    precios = []
    productos = {}
    for key in diccionario:
        letras = []
        for letra in key:
            letras.append(letra)
        if letras[0] == 'c' or letras[0] == 'C':
            precios.append(diccionario[key])
            productos[key] = diccionario[key]
        letras.clear()
    suma = sum(precios)
    print(f"El precio total de los productos que empiezan con 'C' es: {suma}"+
          f"\ny los productos son: {productos}")
# Creación del diccionario con valores ingresados por usuario
diccionario_precios = {}
ingresar_items(diccionario_precios)
