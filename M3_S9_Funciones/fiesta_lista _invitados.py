"""
Se solicita crear un programa en Python que permita llevar el registro de los invitados a una fiesta.
Para ello, se pide crear dos conjuntos (set): uno con los nombres de los invitados confirmados 
y otro con los nombres de los invitados que han llegado a la fiesta.

A medida que los invitados van llegando a la fiesta, se deben ir agregando sus nombres al conjunto de los que asistieron.
Además, se debe imprimir en pantalla la cantidad de invitados confirmados y la cantidad de invitados que han asistido.
Finalmente, se debe imprimir en pantalla el nombre de los invitados que confirmaron su asistencia pero aún no han llegado a la fiesta, 
es decir, los nombres que se encuentran en el conjunto de confirmados pero no en el conjunto de los que asistieron.
"""
def agregar_invitados_confirmados():
    set_confirmados = set() #set vacio para agregar confirmados
    print("Cuantos invitados confirmados desea ingresar")
    confirmados = int(input("Ingrese la cantidad: "))
    for i in range(confirmados): #se recorre el ingreso hasta que se cumpla la cantidad de confirmados necesarios
        set_confirmados.add(input(f"Nombre del {i+1}er invitado: "))
    return set_confirmados

def agregar_invitados_asistentes(set_asistentes):
    print("Ingrese el nombre del invitado: ", end="")
    set_asistentes.add(input())
    return set_asistentes

def cantidad_confirmados_o_asistentes(datos):
    print("La cantidad es",len(datos))
    
def conocer_faltantes(invitados_confirmados,invitados_asistentes):
    faltantes = invitados_confirmados - invitados_asistentes
    print(f"Los invitados faltantes son:",faltantes)
    
def aplicacion_fiesta():
    invitados_confirmados = set()
    invitados_asistentes = set()
    while True:
        opcion = int(input("Hola, bienvenido\n" 
                        "1.- agregar_invitados_confirmados\n" 
                        "2.- agregar_invitados_asistentes\n" 
                        "3.- cantidad_confirmados_o_asistentes\n" 
                        "4.- conocer_faltantes\n" 
                        "5.- Salir\n\n" 
                        "Ingresa una opción => ")
                    )
        
        match opcion: 
            case 1: 
                invitados_confirmados = agregar_invitados_confirmados()
            case 2: 
                invitados_asistentes = agregar_invitados_asistentes(invitados_asistentes)
            case 3:
                print("Desea conocer los invitados asistentes o confirmados")
                print("1.- Asistentes")
                print("2.- Confirmados ", end="")
                ingreso = input()
                if(ingreso == 1): 
                    cantidad_confirmados_o_asistentes(invitados_asistentes)
                else:
                    cantidad_confirmados_o_asistentes(invitados_confirmados)
            case 4: 
                conocer_faltantes(invitados_confirmados,invitados_asistentes)
            case 5: 
                print("Nos vemos!") 
                break 
            case _: 
                print("Esa opcion no es válida!")
                
aplicacion_fiesta()

#crear dos conjuntos (set): uno con los nombres de los invitados confirmados 
# y otro con los nombres de los invitados que han llegado a la fiesta.
#invitados_confirmados = {"Maria","Fulanito","Jose","Cleopatra","Mario","Feliciano"}
#invitados_asistentes = set()

#A medida que los invitados van llegando a la fiesta, se deben ir agregando sus nombres al conjunto de los que asistieron.
# invitados_asistentes.add("Feliciano")
# invitados_asistentes.add("Cleopatra")
# invitados_asistentes.add("Maria")
# invitados_asistentes.add("Jose")
# invitados_asistentes.add("Mario")
# invitados_asistentes.add("Fulanito")

#Además, se debe imprimir en pantalla la cantidad de invitados confirmados y la cantidad de invitados que han asistido.
#print("Los invitados confirmados son: ", len(invitados_confirmados)) 
#print(f"Los invitados asistentes son: {len(invitados_asistentes)}")

#Finalmente, se debe imprimir en pantalla el nombre de los invitados que confirmaron su asistencia pero aún no han llegado a la fiesta, 
#es decir, los nombres que se encuentran en el conjunto de confirmados pero no en el conjunto de los que asistieron.

#invitados_faltantes = invitados_confirmados - invitados_asistentes
#invitados_faltantes = invitados_confirmados.symmetric_difference(invitados_asistentes)
#invitados_faltantes = invitados_confirmados ^ invitados_asistentes
#invitados_faltantes = invitados_confirmados.difference(invitados_asistentes)
#print(invitados_faltantes)





