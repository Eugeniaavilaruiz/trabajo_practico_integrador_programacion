def validar_nombre(nombre):
    """Valida el nombre de una herramienta ingresado por el usuario.
 
    Le quita los espacios del principio y del final.
    Parámetro: nombre (texto escrito por el usuario).
    Devuelve: el nombre sin espacios sobrantes.
    Lanza ValueError si el nombre queda vacío o si no contiene ninguna letra.
    """
    nombre = nombre.strip()
    if nombre == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
    tiene_letra = False  # bandera
    for caracter in nombre:
        if caracter.isalpha():
            tiene_letra = True
    if not tiene_letra:
        raise ValueError("El nombre de la herramienta debe contener al menos una letra.")
    return nombre
 
 
def buscar_herramienta(nombre, inventario):
    """Busca una herramienta en el inventario por su nombre.
 
    Compara sin tener en cuenta mayúsculas ni espacios sobrantes.
    Parámetros: nombre (texto a buscar) e inventario (lista de herramientas).
    Devuelve: el diccionario de la herramienta si la encuentra, o None si no existe.
    """
    for producto in inventario:
        if producto["herramienta"].strip().lower() == nombre.strip().lower():
            return producto
    return None

def cargar_herramientas(inventario):
    """Opción 1: carga varias herramientas con su stock inicial.

    Pide cuántas herramientas se van a cargar y, por cada una, el nombre y el stock.
    Los errores se capturan dentro de la función y se vuelve a pedir solo el dato inválido.
    Cada herramienta se agrega a inventario recién cuando el nombre y el stock son válidos.
    Parámetro: inventario (lista de herramientas).
    """
    while True:
        try:
            cantidad_herramientas = int(input("¿Cuántas herramientas vas a cargar? "))
            if cantidad_herramientas <= 0:
                raise ValueError("La cantidad debe ser un número mayor que 0.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    for i in range(cantidad_herramientas):
        print(f"--- Herramienta {i + 1} de {cantidad_herramientas} ---")
        while True:
            try:
                nombre = validar_nombre(input("Nombre: "))
                if buscar_herramienta(nombre, inventario) != None:
                    raise ValueError(f"La herramienta '{nombre}' ya existe en el inventario.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        while True:
            try:
                stock = int(input(f"Stock inicial de {nombre}: "))
                if stock < 0:
                    raise ValueError("El stock no puede ser negativo.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        inventario.append({'herramienta': nombre, 'cantidad': stock})
        print(f"Se dio de alta '{nombre}' con {stock} unidades.")


def mostrar_inventario(inventario):
    """Opción 2: muestra todas las herramientas con su stock actual.

    Si el inventario está vacío, lo informa con un mensaje.
    Parámetro: inventario (lista de herramientas).
    """
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
        return  # sale de la función y vuelve al menú
    for producto in inventario:
        print(f"{producto['herramienta']}: {producto['cantidad']} unidades")


def consultar_stock(inventario):
    """Opción 3: muestra el stock de una herramienta buscada por nombre.

    Si el inventario está vacío o la herramienta no existe, lo informa con un mensaje.
    Un nombre vacío lanza ValueError, que se captura en main().
    Parámetro: inventario (lista de herramientas).
    """
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
        return
    nombre = validar_nombre(input("Ingresa el nombre de la herramienta: "))
    producto = buscar_herramienta(nombre, inventario)
    if producto == None:
        print(f"La herramienta '{nombre}' no existe en el inventario.")
    else:
        print(f"{producto['herramienta']}: {producto['cantidad']} unidades")


def reporte_agotados(inventario):
    """Opción 4: muestra las herramientas con stock cero.

    Usa una bandera para saber si encontró alguna. Si no hay ninguna agotada,
    muestra un mensaje distinto al de inventario vacío.
    Parámetro: inventario (lista de herramientas).
    """
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
        return
    hay_agotados = False  # bandera
    for producto in inventario:
        if producto['cantidad'] == 0:
            print(f"{producto['herramienta']} está agotada")
            hay_agotados = True
    if not hay_agotados:
        print("No hay productos agotados.")


def alta_producto(inventario):
    """Opción 5: agrega una herramienta nueva al final del inventario.

    Primero valida el nombre y recién después pide el stock inicial.
    Lanza ValueError si el nombre está vacío o repetido, o si el stock es negativo;
    int() lanza ValueError si el stock no es un número entero.
    Los errores se capturan en main() y no se agrega nada.
    Parámetro: inventario (lista de herramientas).
    """
    nombre = validar_nombre(input("Ingresa el nombre de la herramienta que deseas dar de alta: "))
    if buscar_herramienta(nombre, inventario) != None:
        raise ValueError(f"La herramienta '{nombre}' ya existe en el inventario.")
    stock = int(input(f"Ingresa las unidades para {nombre}: "))
    if stock < 0:
        raise ValueError("El stock no puede ser negativo.")
    inventario.append({'herramienta': nombre, 'cantidad': stock})
    print(f"Se dio de alta '{nombre}' con {stock} unidades.")


def actualizar_stock(inventario):
    """Opción 6: registra una venta (resta stock) o un ingreso (suma stock).

    Valida en orden: inventario vacío, nombre, que la herramienta exista,
    tipo de movimiento, unidades mayores que 0 y, si es venta, que haya stock suficiente.
    Recién cuando todo es válido modifica el stock.
    Parámetro: inventario (lista de herramientas).
    """
    if len(inventario) == 0:
        print("No hay herramientas cargadas.")
        return
    nombre = validar_nombre(input("Ingresa el nombre de la herramienta a actualizar: "))
    producto = buscar_herramienta(nombre, inventario)
    if producto == None:
        print(f"La herramienta '{nombre}' no existe en el inventario.")
        return
    print("1. Ingreso")
    print("2. Venta")
    tipo = input("Tipo de movimiento: ").strip()
    if tipo != "1" and tipo != "2":
        print("Tipo de movimiento inválido. Debe ser 1 (Ingreso) o 2 (Venta).")
        return
    unidades = int(input("Cantidad de unidades: "))
    if unidades <= 0:
        raise ValueError("Las unidades deben ser un número mayor que 0.")
    if tipo == "2":  # venta
        if unidades > producto['cantidad']:
            raise ValueError(f"Stock insuficiente: hay {producto['cantidad']} unidades de {producto['herramienta']} y quisiste vender {unidades}.")
        producto['cantidad'] = producto['cantidad'] - unidades
    else:  # ingreso
        producto['cantidad'] = producto['cantidad'] + unidades
    print(f"Stock actualizado: {producto['herramienta']} ahora tiene {producto['cantidad']} unidades.")


def main():
    """Función principal: crea el inventario y muestra el menú hasta elegir la opción 7.

    Captura los ValueError que llegan de las opciones (menú inválido y opciones 3, 5 y 6),
    muestra el motivo y vuelve a mostrar el menú.
    """
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