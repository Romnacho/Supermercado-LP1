import os
from src.almacen.almacen import Almacen
from src.almacen.inventario import Inventario
from src.carrito.carrito import Carrito
from src.cliente.cliente import Cliente
from src.pedidos.proveedor import Proveedor
from src.gondola.gondola import Gondola
from src.hardware.lectordecodigo import LectorDeCodigoDeBarras
from src.menu.simulacion import simulacionDeCompra

"""Menu principal, se accede a distintas funcionalidades del sistema
Llevan a distintos submenús, una simulacion de un cliente y para salir del codigo
Todos tienen para salir en 11 por comodidad del usuario"""

def menu_principal(almacen : Almacen, carrito : Carrito, cliente : Cliente, proveedor : Proveedor, inventario : Inventario, lector : LectorDeCodigoDeBarras):
    limpiar()
    while True:
        print("\n=== BIENVENIDO AL SUPERMERCADO ===")
        print("1. Ver góndolas")
        print("2. Ver carrito")
        print("3. Pagar")
        print("4. Simular cliente")
        print("11. Salir")
        opcion = input("\nElegí una opción: ")

        """switch case del menu principal"""

        if opcion == "1":
            menu_gondolas(almacen, carrito, proveedor, inventario)
        elif opcion == "2":
            menu_carrito(carrito, inventario)
        elif opcion == "3":
            if len(carrito.getListaProductos()) == 0:
                print("\nEl carrito está vacío!")
                continuar()
            else:
                cliente.pagar()
                continuar()
                break
        elif opcion == "4":
            simulacionDeCompra(lector, almacen, carrito, proveedor, inventario, cliente)
            carrito.vaciarCarrito()
            continuar()
        elif opcion == "11":
            print("\nHasta luego!")
            break
        else:
            print("\nOpción inválida, intentá de nuevo")
            continuar()

"""Submenu de la gondola, imprime todas las gondolas al cliente, permitirle entrar e interactuar con cada una para revisar los productos"""

def menu_gondolas(almacen : Almacen, carrito : Carrito, proveedor : Proveedor, inventario : Inventario):
    limpiar()
    while True:
        print("\n=== GÓNDOLAS DISPONIBLES ===")
        gondolas = almacen.getListaGondolas()
        for i, gondola in enumerate(gondolas):
            promo = f"- PROMO ACTIVA: {gondola.getPromoDescripcion()}" if gondola.getPromo() != 0 else ""
            print(f"{i+1}. {gondola.getTipo()} {promo}")
        print("11. Volver")

        opcion = input("\nElegí una góndola: ")
        if opcion == "11":
            limpiar()
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(gondolas):
            menu_gondola_individual(almacen, carrito, proveedor, inventario, gondolas[int(opcion)-1])
        else:
            print("\nOpción inválida, intentá de nuevo")

"""Submenu de cada gondola, permite revisar los productos, añadirlos al carrito y volver al menu de gondolas"""

def menu_gondola_individual(almacen : Almacen, carrito : Carrito, proveedor : Proveedor, inventario : Inventario, gondola : Gondola):
    limpiar()
    while True:
        print(f"\n=== {gondola.getTipo().upper()} ===")
        if gondola.getPromo() != 0:
            print(f"PROMO: {gondola.getPromoDescripcion()}")
        print("\n1. Ver productos")
        print("2. Agregar producto al carrito")
        print("11. Volver")

        opcion = input("\nElegí una opción: ")

        if opcion == "1":
            mostrar_productos(gondola)
            continuar()
            limpiar()
        elif opcion == "2":
            agregar_producto(almacen, carrito, proveedor, inventario, gondola)
            limpiar()
        elif opcion == "11":
            limpiar()
            break
        else:
            print("\nOpción inválida, intentá de nuevo")

"""Muestra los productos"""

def mostrar_productos(gondola : Gondola):
    limpiar()
    print(f"\n=== PRODUCTOS EN {gondola.getTipo().upper()} ===")
    productos = gondola.getProductos()
    for i, producto in enumerate(productos):
        print(f"\n{i+1}. {producto}")
        print("-" * 40)

"""Muestra los productos y permite añadirlos al carrito"""

def agregar_producto(almacen : Almacen, carrito : Carrito, proveedor : Proveedor, inventario : Inventario, gondola : Gondola):
    mostrar_productos(gondola)
    productos = gondola.getProductos()
    opcion = input("\nElegí un producto (o 0 para volver): ")

    """Si es 0 se vuelve, sino pones la cantidad de unidades /kilos que queres comprar y se suman al carrito"""

    if opcion == "0":
        return
    elif opcion.isdigit() and 1 <= int(opcion) <= len(productos):
        producto = productos[int(opcion)-1]

        """Aca se añaden al carrito, depende si son por unidad o por peso el metodo puede variar un poco pero la logicsa es la misma
        se chequea la cantidad, se valida, se procesa el escaneo, se añade al carrito, se fija si tengo que llamar al proveedor y si lo llamo se repone en la gondola"""
        
        if producto.getTipoProducto() == "Peso":
            cantidad = input(f"¿Cuántos kilos de {producto.getNombre()}? ")
            if not cantidad.replace(".", "", 1).isdigit() or float(cantidad) <= 0:
                print("\nCantidad inválida")
                return
            cantidad = float(cantidad)
            print(f"\n Kilos de {producto.getNombre()} agregados al carrito")
            print(f"\n Kilos disponibles en góndola: {producto.getStock() - cantidad} kg")
        else:
            cantidad = input(f"¿Cuántos paquetes de {producto.getNombre()}?")
            if not cantidad.isdigit() or int(cantidad) <= 0:
                print("\nCantidad inválida")
                return
            cantidad = int(cantidad)
            print(f"\n Paquetes de {producto.getNombre()} agregados al carrito")
            print(f"\n Stock disponible en góndola: {producto.getStock() - cantidad} unidades")
            
        cantidad = float(cantidad)
        pedido = almacen.procesarEscaneo(producto.getCodigoBarras(), carrito, cantidad)
        if pedido is False:
            continuar()
            return
        print(f"\n✓ {producto.getNombre()} agregado al carrito!")
        continuar()

"""Menu carrito, muestra los productos que hay, permite eliminar los productos y volver al menu principal, si esta vacio no te muestra nada"""

def menu_carrito(carrito : Carrito, inventario : Inventario):
    limpiar()
    while True:
        print("\n=== TU CARRITO ===")
        if len(carrito.getListaProductos()) == 0:
            print("El carrito está vacío")
            continuar()
            break

        productos = carrito.getListaProductos()
        for i, (producto, precio, cantidad) in enumerate(productos):
            print(f"{i+1}. {producto.getNombre()} x {cantidad} - ${precio}")
        print(f"\nTotal: ${carrito.getTotalAcumulado()}")
        print("\n1. Eliminar producto")
        print("11. Volver")

        """Si el usuario elige eliminar un producto se le pregunta cual quiere borrar, introduce el indice del producto que aparece a su izquierda y se borra
        Despues se devuelve el stock a la gondola o al deposito, si se llena la gondola y aun sobra stock se manda al deposito"""

        opcion = input("\nElegí una opción: ")
        if opcion == "1":
            opcion_eliminar = input("¿Qué producto querés eliminar? ")
            if opcion_eliminar.isdigit() and 1 <= int(opcion_eliminar) <= len(productos):
                producto, precio, cantidad = productos[int(opcion_eliminar)-1]
                carrito.eliminarProducto(producto, precio, cantidad)
                if producto.getStock() + cantidad <= producto.getStockMaximo():
                    producto.actualizarStock(-cantidad)  #devuelve a la gondola
                else:
                    inventario.getDeposito().agregarStock(producto.getCodigoBarras(), cantidad)  #manda al deposito
                print(f"\n✓ {producto.getNombre()} eliminado del carrito")
                continuar()
            else:
                print("\nOpción inválida")
        elif opcion == "11":
            limpiar()
            break
        else:
            print("\nOpción inválida")

"""Limpian la terminal para dejarla pipi cucu"""

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def continuar():
    input("\nPresioná Enter para continuar...")
    limpiar()