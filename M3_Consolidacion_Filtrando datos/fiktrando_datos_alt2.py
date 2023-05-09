""" Dada la siguiente lista de nombres:
• Harry Houdini
• Newton
• David Blaine
• Hawking
• Messi
• Teller
• Einstein
• Pele
• Juanes
Y sabiendo que Harry Houdini, David Blaine y Teller son magos. Y también que Newton, Hawking y
Einstein son científicos. Debemos separar los nombres en tres grupos: magos, científicos y otros; y
escribir una función llamada hacer_grandioso(), que modifique la lista de magos añadiendo la
frase ‘El gran‘ antes del nombre de cada mago.
Crear una función llamada imprimir_nombres(), que imprime el nombre de cada persona de la
lista.
Finalmente, imprimir en pantalla la lista completa de nombres antes de ser modificados; luego
imprimir los nombres de los magos grandiosos, los nombres de los científicos, y los restantes """

# Funciones se definen en la parte superior,
# sobretodo si es desarrollo backend de un sólo archivo

########################################################################
# DEFINIENDO FUNCIONES QUE GENERAN LAS LISTAS O DICCIONARIO


def creacion_diccionario(lista, magos, cientificos, otros):
    """ Función que retorna un diccionario con los elementos originales """
    for nombre in lista:
        if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(nombre)
        elif nombre in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(nombre)
        else:
            otros.append(nombre)
    diccionario_nombres = {'Magos': magos,
                           'Cientificos': cientificos, 'Otros': otros}
    return diccionario_nombres


def creacion_sublistas(lista, magos, cientificos, otros):
    """ Función que retorna una lista con sublista de las categorias """
    for nombre in lista:
        if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(nombre)
        elif nombre in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(nombre)
        else:
            otros.append(nombre)
    lista_nombres = {magos, cientificos, otros}
    return lista_nombres


def creacion_listas(lista):
    """ Función que retorna tres listas independientes con los nombres categorizados """
    magos = cientificos = otros = []
    for persona in lista:
        if persona in ['Harry Houdini', 'David Blaine', 'Teller']:
            magos.append(persona)
        elif persona in ['Newton', 'Hawking', 'Einstein']:
            cientificos.append(persona)
        else:
            otros.append(persona)
    print(magos)
    print(cientificos)
    print(otros)

########################################################################
# FUNCIONES REQUERIDAS


def hacer_grandioso_lista_general_definida(lista):
    """ Función que añade la frase ‘El gran‘ antes del nombre de cada mago 
    EN UNA LISTA COMPLETA DE NOMBRES GENERALES"""
    lista_magos = []  # define lista de magos
    # extrae los magos de la lista general
    for nombre in lista:
        if nombre in ['Harry Houdini', 'David Blaine', 'Teller']:
            lista_magos.append(nombre)
    # modifica la nueva lista de magos generada
    i = 0
    for mago in lista_magos:
        mago = "El gran " + mago
        lista_magos[i] = mago
        i += 1
    # imprime la nueva lista de magos grandiosos
    imprimir_nombres(lista_magos)


def hacer_grandioso_lista_magos_generada(lista):
    listas_generadas = creacion_listas(lista)
    # modifica la nueva lista de magos generada
    i = 0
    for mago in magos:
        mago = "El gran " + mago
        magos[i] = mago
        i += 1
    # imprime la nueva lista de magos grandiosos
    imprimir_nombres(mago)


def imprimir_nombres(lista):
    """ Imprime el nombre de cada persona de la lista """
    lista_nueva = []
    for persona in lista:
        print(persona)
        lista_nueva.append(persona)
    # print(lista_nueva)


########################################################################
# EJEMPLOS DE LAS LISTAS Y DICCIONARIO YA GENERADOS

# Ejemplo con solo una lista
lista_p1 = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking',
            'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

# Ejemplo con sublistas
lista_p2 = [['Harry Houdini', 'David Blaine', 'Teller'],
            ['Newton', 'Hawking', 'Einstein'],
            ['Messi', 'Pele', 'Juanes']]

# Ejemplo con diccionario
diccionario_p = {
    'Magos': ['Harry Houdini', 'David Blaine', 'Teller'],
    'Cientificos': ['Newton', 'Hawking', 'Einstein'],
    'Otros': ['Messi', 'Pele', 'Juanes']
}

########################################################################
# DESARROLLO DEL EJERCICIO, PARA GENERAR LOS RESULTADOS

# hacer_grandioso_lista_general_definida(lista_p1)
print(creacion_listas(lista_p1))
