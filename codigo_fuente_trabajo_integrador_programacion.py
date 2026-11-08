def validar_nombre(nombre):
    nombre = nombre.strip()
    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
    return nombre


def buscar_herramienta(nombre, inventario):
    for producto in inventario:
        if producto["herramienta"].strip().lower() == nombre.strip().lower():
            return producto
    return None


def cargar_herramientas(inventario):
    print('Opción 1 en construcción')


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas")
        return  # sale de la función y vuelve al menú
    for producto in inventario:
        print(f"{producto['herramienta']}: {producto['cantidad']} unidades")


def consultar_stock(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas")
        return
    nombre = validar_nombre(input("Ingresa el nombre de la herramienta: "))
    producto = buscar_herramienta(nombre, inventario)
    if producto == None:
        print(f"La herramienta '{nombre}' no existe en el inventario.")
    else:
        print(f"{producto['herramienta']}: {producto['cantidad']} unidades")


def reporte_agotados(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas")
        return
    hay_agotados = False  # bandera
    for producto in inventario:
        if producto['cantidad'] == 0:
            print(f"{producto['herramienta']} está agotada")
            hay_agotados = True
    if not hay_agotados:
        print("No hay productos agotados")


def alta_producto(inventario):
    nombre = validar_nombre(input("Ingresa el nombre de la herramienta que deseas dar de alta: "))
    if buscar_herramienta(nombre, inventario) != None:
        raise ValueError(f"La herramienta '{nombre}' ya existe en el inventario.")
    stock = int(input(f"Ingresa las unidades para {nombre}: "))
    if stock < 0:                                              
        raise ValueError("El stock no puede ser negativo.")
    inventario.append({'herramienta': nombre, 'cantidad': stock})
    print(f"Se dio de alta '{nombre}' con {stock} unidades.")

    
def actualizar_stock(inventario):
    if len(inventario) == 0:
        print("No hay herramientas cargadas")
        return
    nombre = validar_nombre(input("Ingresa el nombre de la herramienta que deseas actualizar stock: "))
    producto = buscar_herramienta(nombre, inventario)
    if producto == None:
        print(f"La herramienta '{nombre}' no existe en el inventario.")
        return
    print("1. Ingreso")
    print("2. Venta")
    opcion = input("Ingresa la opcion que deseas hacer: ").strip()
    if opcion != "1" and opcion != "2":
        print("Tipo de movimiento inválido. Debe ser 1 (Ingreso) o 2 (Venta).")
        return
    unidades = int(input("Cantidad de unidades: "))
    if unidades <= 0:
        raise ValueError("Las unidades deben ser un número mayor que 0.")
    if opcion == "2":                                
        if unidades > producto['cantidad']:
            raise ValueError(f"Stock insuficiente: hay {producto['cantidad']} unidades de {producto['herramienta']} y quisiste vender {unidades}.")
        producto['cantidad'] = producto['cantidad'] - unidades
    else:                                             
        producto['cantidad'] = producto['cantidad'] + unidades
    print(f"Stock actualizado: {producto['herramienta']} ahora tiene {producto['cantidad']} unidades.")


def main():
    inventario = []
    opcion = 0
    print('Sistema de inventario iniciado')
    while opcion != 7:
        try:
            print("-----MENÚ-----")
            print("1. Carga de herramientas")
            print("2. Visualización de inventario")
            print("3. Consulta de stock")
            print("4. Reporte de agotados")
            print("5. Alta de nuevo producto")
            print("6. Actualización de stock (venta / ingreso)")
            print("7. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion != 7:
                raise ValueError("Opción fuera de rango (1 a 7).")
        except ValueError as e:
            print(f"Error: {e}")
    print("Fin del programa")


main()