#Una transportadora requiere el desarrollo de una aplicacion que permita llevar un registro de los despachos de un vehiculo teniendo en cuenta lo siguiente:

#-Placa del vehiculo
#-Placa de descripcion del vehiculo
#-Nombre del conductor
#-Contacto del conductor
#-Ruta

#-Descripcion de la carga; el numero de despacho se genera de forma automatica, es decir una variable incrementable. Dicha informacion debe queda registrada en un diccionario.

#El sistema debe realizar:

#Registro de salidas y mostrar salir

# Registro de despachos de vehiculo

# Diccionario para almacenar los datos de los despachos

registro_despachos = {}
numero_despacho = 1

def registrar_salida():
    global numero_despacho
    try:
        # Preguntas basicas  
        placa_vehiculo = input("Ingrese la Placa del vehiculo: ")
        descripcion_vehiculo = input("Ingrese la Placa de descripcion del vehiculo: ")
        nombre_conductor = input("Ingrese el Nombre del conductor: ")
        contacto_conductor = input("Ingrese el Contacto del conductor: ")
        ruta = input("Ingrese la Ruta: ")
        carga = input("Ingrese la Descripcion de la carga: ")

        despacho = {
            "Placa del vehiculo": placa_vehiculo,
            "Placa de descripcion del vehiculo": descripcion_vehiculo,
            "Nombre del conductor": nombre_conductor,
            "Contacto del conductor": contacto_conductor,
            "Ruta": ruta,
            "Carga": carga
        }
        #Recomendacion de boxblack
        registro_despachos[numero_despacho] = despacho
        numero_despacho += 1
        print("Registro de salida exitoso.")
    except Exception as e:
        print("Ha ocurrido un error:", e)

def mostrar_salidas():
    print("--- REGISTRO DE SALIDA ---")
    if registro_despachos:
        for numero_despacho, despacho in registro_despachos.items():
            print(f"Número de Despacho: {numero_despacho}")
            for clave, valor in despacho.items():
                print(f"{clave}: {valor}")
            print("--------------------------")
    else:
        print("No hay registros de salida.")

# Menú principal para que le pregunte al usuario cuando quiera ingresar o ver las salidas :P
while True:
    print("\n ---MENU PRINCIPAL DE REGISTRO --- :")
    print("1. Registro de salida")
    print("2. Mostrar salidas")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_salida()
    elif opcion == "2":
        mostrar_salidas()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción que si sea válida para hacer el registro.")
