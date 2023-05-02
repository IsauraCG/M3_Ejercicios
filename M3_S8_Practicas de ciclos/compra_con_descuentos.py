
# Imprime una lista de los precios en una lista de precios, con un descuento del 10%

precios = [25.50, 12.30, 36.40, 9.75, 15.20]
descuento = []

for i in precios:
    i = i - (i*0.1)
    descuento.append(i)

print(descuento)  # imprime las lista precios con el descuento.

# imprime sumatoria de precios con descuento redondeado
print(f"{sum(descuento):.2f}")
