""" Requerimos crear un registro de datos personales de tres personas. 
Los datos que se necesitan son: su nombre, apellido y teléfono. 
Para ello, generaremos un diccionario para cada una de las personas con los datos mencionados, 
y luego los almacenaremos dentro de una lista. 
Finalmente, imprimiremos en pantalla la lista. """

#Crear un registro de datos personales de tres personas
# con datos: nombre, apellido y teléfono

#Generaremos un diccionario para cada una de las personas con los datos mencionados

dict_pers_1 = { 'nombre' : 'Juanita', 'apellido' : 'Pérez', 'teléfono' : '+5691234678' }
dict_pers_2 = { 'nombre' : 'Fernando', 'apellido' : 'Ramírez', 'teléfono' : '+56876543219' }
dict_pers_3 = { 'nombre' : 'Marcelo', 'apellido' : 'Henríquez', 'teléfono' : '+56765432198' }

#Los almacenaremos dentro de una lista
lista_personas = [dict_pers_1,dict_pers_2,dict_pers_3]

#imprimiremos en pantalla la lista
print(f"La lista de personas con sus datos requeridos es la siguiente:{lista_personas}")
print(f"Un mejor formato sería: \n{dict_pers_1['nombre'],dict_pers_1['apellido'],dict_pers_1['teléfono']}\n{dict_pers_2['nombre'],dict_pers_2['apellido'],dict_pers_2['teléfono']}\n{dict_pers_3['nombre'],dict_pers_3['apellido'],dict_pers_3['teléfono']}")