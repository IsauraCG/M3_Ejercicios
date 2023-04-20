print(1, 2, 3)
#Con comas de separacion
print(1, 2, 3, sep = ', ')
#Símbolo al final
print(1 + 2, end=' - ')
#prioridades aritmeticas
print((2 + 3) * 5)
#Indentacion en Python
if True:
    print("Hola mundo")
    print(type(2+5))
    if True:
        cadena = "String"
        print(cadena)

#tipos de datos
'''Como sonsultar tipos de datos en python'''
print(type(5)) #int <class 'int'>
print(type(cadena)) #str <class'str'>
print(type("2"))#str <class'str'>
print(type(True)) #bool <class 'bool'> 
print(type(False)) #bool <class 'bool'>
print(type([])) #list <class 'list'>
print(type(2 + 1j))#complex <class 'complex'>
print(type(None))#None <class 'NoneType'>
print(type(1.5))#float <class 'float'>

# Distintos modos de formato para impresión
a = 1
b = 2
c = 3
print(c)
print("El valor es:", c)
print(f"El valor es: {c}")
print("El valor es: {} {} {}".format(c, a*b, a))