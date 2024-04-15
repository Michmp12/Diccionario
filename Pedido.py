import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_pedido(pedidos):
    limpiar_pantalla()
    print(" ---- REGISTRO DE PEDIDO ---- ")
    nombre_cliente = input("Ingrese por favor el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    sexo = input("Ingrese el sexo del cliente (F/M): ")
    descripcion_lugar = input("Ingrese la descripción del lugar: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    referencia_producto = input("Ingrese la referencia del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto deseado: "))

    if nombre_cliente not in pedidos:
        pedidos[nombre_cliente] = []
    pedido = {
        "direccion": direccion,
        "contacto": contacto,
        "sexo": sexo,
        "descripcion_lugar": descripcion_lugar,
        "productos": [{
            "nombre_producto": nombre_producto,
            "referencia_producto": referencia_producto,
            "cantidad": cantidad
        }]
    }
    pedidos[nombre_cliente].append(pedido)
    print("Pedido registrado con éxito.")
    input("Presione Enter para volver al menú...")

def ver_pedidos(pedidos):
    limpiar_pantalla()
    print(" ---- LISTADO DEL PEDIDO ----")
    if not pedidos:
        print("Lo siento pero no hay pedidos registrados.")
    else:
        for cliente, lista_pedidos in pedidos.items():
            print(f"Cliente: {cliente}")
            for pedido in lista_pedidos:
                print("Dirección:", pedido["direccion"])
                print("Contacto:", pedido["contacto"])
                print("Sexo:", pedido["sexo"])
                print("Descripción del lugar:", pedido["descripcion_lugar"])
                print("Productos:")
                for producto in pedido["productos"]:
                    print("- Nombre:", producto["nombre_producto"])
                    print("  Referencia:", producto["referencia_producto"])
                    print("  Cantidad:", producto["cantidad"])
                print("--------------------")
    input("Presione ENTER para volver al menú principal...")

def menu():
    pedidos = {}
    while True:
        limpiar_pantalla()
        print(" ---- MENU ---- ")
        print("1. Registrar pedido")
        print("2. Mostrar los pedidos")
        print("3. Salir")
        opcion = input("Seleccione una opción por favor: ")
        if opcion == "1":
            registrar_pedido(pedidos)
        elif opcion == "2":
            ver_pedidos(pedidos)
        elif opcion == "3":
            break
        else:
            print("Lo siento la opción es inválida, Intentalo nuevamente.")
            input("Presione ENTER para continuar...")

menu()

