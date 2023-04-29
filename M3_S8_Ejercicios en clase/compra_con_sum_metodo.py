# Imprimir la sumatoria de una lista de precios con descuento del 10%

compra = [25.50, 12.30, 36.40, 9.75, 15.20]

# imprime la sumatoria de los precios en lista 'compra' con formato aproximado a 2 decimales
print(f"{sum(compra):.2f}")

# después, declara la lista con descuento, y dentro, la operación que define los elementos en la lista
# en este caso: (se multiplica 'precio' x 0.9 ) por cada uno de los elementos 'precio' en lista 'compra'
with_desc = [precio * 0.9 for precio in compra]

# imprime la nueva lista de los precios con descuento
print(with_desc)

# imprime la nueva suma total de la compra con descuento
print(f"La suma con descuento es {sum(with_desc):.2f}")
