import os
n_Despachos = 0
diccionario_registo = {}
sw = True
def fnt_agregar(diccionario, placa, descripcion_vehiculo, nombre, contacto, ruta, descripcion_carga  ):
    global n_Despachos
    if placa == '' or descripcion_vehiculo == '' or nombre == '' or contacto == '' or ruta == '' or descripcion_carga == '':
        enter = input('debe de diligenciar toda la informacion solicitadad <ENTER>')
    else :
        diccionario[placa] = {'Descipción del vehiculo': descripcion_vehiculo, 'nombre': nombre, 'contacto': contacto, 'ruta': ruta, 'descripcion de la carga': descripcion_carga}
        n_Despachos += 1
    enter = input(f'\nEl vehiculo {placa} ha sido registrado con exito <ENTER>')


def fnt_consultar():
    global diccionario_registo
    os.system('cls')
    print('\nCantidad de registros: ',n_Despachos,'\n')
    for key, valor in diccionario_registo.items():
        print(f'Numero de placa: {key}')
        print(f'{valor}')
    enter = input('\n\nPresione ENTER para continuar...')


def fnt_selector(opcion):
    global sw
    global diccionario_registo

    if opcion == '1':
        os.system('cls')
        nombre = input('Nombre del conductor: ')
        placa = input('número de placa del vehiculo: ')
        contacto = input('Número de contacto: ')
        descripcion_vehiculo = input('Descrión del vehiculo: ')
        descripcion_carga = input('Descripción de carga: ')
        ruta = input('Ruta a recorrer: ')
        fnt_agregar (diccionario_registo, placa, descripcion_vehiculo, nombre, contacto, ruta, descripcion_carga)

    elif opcion == '2':
        fnt_consultar()

    elif opcion == '3':
        sw = False


while sw == True: 
    os.system('cls')
    opcion = input('1. Registrar\n2. Mostrar\n3. Salir\n- >  ')
    fnt_selector(opcion)
