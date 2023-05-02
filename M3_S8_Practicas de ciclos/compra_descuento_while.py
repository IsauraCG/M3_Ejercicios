
# Mostrar la suma de estos precios con un 10% de descuento
lista = [25.50, 12.30, 36.40, 9.75, 15.20]

# se declara variable iteración
i = 0
# se declara variable que acumula la suma.
suma = 0

while i < len(lista):
    suma += lista[i]
    i += 1

print(f"El valor total de la compra es: $ {(suma):.2f}")
print(f"Y con el 10% de descuento queda en: $ {(suma * 0.9):.2f}")
