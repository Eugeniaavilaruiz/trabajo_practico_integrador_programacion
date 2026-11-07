def validar_nombre(nombre):
    nombre = nombre.strip()
    if nombre == "":
        raise ValueError("El campo no puede estar vacio")
    return nombre

def buscar_herramienta(inventario, nombre):
    for producto in inventario:
        if producto["herramienta"].strip().lower() == nombre.strip().lower():
            return producto
    return None

def cargar_herramientas(inventario):
    print('Opción 1 en construcción')


def mostrar_inventario(inventario):
    print('Opción 2 en construcción')


def consultar_stock(inventario):
    print('Opción 3 en construcción')


def reporte_agotados(inventario):
    print('Opción 4 en construcción')


def alta_producto(inventario):
    print('Opción 5 en construcción')


def actualizar_stock(inventario):
    print('Opción 6 en construcción')


def main():
    inventario = []
    opcion = 0
    print('Sistema de inventario iniciado')
    while opcion != 7:
        try:
            print("-----MENU-----")
            print("1. Carga herramientas")
            print("2. Visualización de inventario")
            print("3. Consulta de stock")
            print("4. Reporte de agotados")
            print("5. Alta de nuevo producto")
            print("6. Actualización de stock (venta / ingreso)")
            print("7. Salir")
            opcion = int(input("Seleccione una opcion: "))
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
                raise ValueError("Opción fuera de rango (1 a 7).") #
            
        except ValueError as e:
            print(f"Error: {e}")   
    print("Fin del programa")
    


main()