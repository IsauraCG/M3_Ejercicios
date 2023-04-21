#Para imprimir variables combinadas con texto usando la función print() podemos hacerlo de dos
#formas diferentes.
#La primera de ellas es separar el texto en comillas, y las variables con el símbolo más ( + ), antes y
#después de la variable. Para que este método funcione el valor de la variable debe ser tipo cadena. 

cantidad = "dos"
print("Hoy comí " + cantidad + " helados")

#La otra forma nos permite imprimir variables de cualquier tipo. Para ello, antes de abrir las comillas
#dentro de la función print(), debemos agregar la letra f, y luego dentro de las comillas donde
#necesitemos colocar las variables encerraremos a éstas dentro de llaves ( { } ).

cantidad = 2
print(f"Hoy comí {cantidad} helados")

