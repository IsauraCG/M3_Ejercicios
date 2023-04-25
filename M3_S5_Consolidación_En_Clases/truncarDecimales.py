# Varias formas de limitar cantida de decimales que se imprimen en terminal

import math  # se importa math
var = 54.125645332

# La forma clásica de hacerlo
print("Acortar cifras decimales, la forma clásica de hacerlo: \n"
      "Si var = 54.125645332 - Se muestra: %.3f \n" % var)  # 3 decimales , 3f - la 'f' es por float

# Dando formato a la impresión
print("Acortar cifras decimales dando formato, el cual además la aproxima : \n"
      f"Si var = 54.125645332 - Se muestra: {var:.2f}\n")  # 2 decimales

# Aproximando con método round
print("Acortar cifras decimales aproximándolas con el metodo round() : \n"
      f"Si var = 54.125645332 - Se muestra: {round(var)}\n")  # 2 decimales

# con método math.trun()
print("Acortar cifras decimales con método math.trunc() : \n"
      f"Si var = 54.125645332 - Se muestra: {math.trunc(var)} \n")  # sin decimales

# truncar via cambiar tipo float, a integer (de coma flotante decimal a tipo entero)
print("Acortar cifras decimales parseando a integer : \n"
      f"Si var = 54.125645332 - Se muestra: {int(var)} \n")  # sin decimales
