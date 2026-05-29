from src.almacen.inventario import Inventario
from src.almacen.almacen import Almacen
from src.carrito.carrito import Carrito
from src.cliente.cliente import Cliente
from src.pedidos.proveedor import Proveedor
from src.hardware.lectordecodigo import LectorDeCodigoDeBarras


def simulacionDeCompra(lector : LectorDeCodigoDeBarras, almacen : Almacen, carrito : Carrito, proveedor : Proveedor, inventario : Inventario, cliente : Cliente):
    # SIMULACION DE COMPRA
    print("=== INICIO DE COMPRA ===\n")

    # BEBIDAS
    print("--- Sector Bebidas ---")
    codigo = lector.leerCodigo(1001)
    almacen.procesarEscaneo(codigo, carrito, cantidad=1)
    
    # CARNICERIA
    print("--- Sector Carniceria ---")
    codigo = lector.leerCodigo(2001)  # asado
    almacen.procesarEscaneo(codigo, carrito, cantidad=1)

    # FIAMBRERIA
    print("--- Sector Fiambreria ---")
    codigo = lector.leerCodigo(4001)  # jamon cocido
    almacen.procesarEscaneo(codigo, carrito, cantidad=1)

    # GALLETITAS - PROMO 2x1
    print("--- Sector Galletitas (Promo 2x1) ---")
    codigo = lector.leerCodigo(5001)  # oreo
    almacen.procesarEscaneo(codigo, carrito, cantidad=2)

    # LIMPIEZA
    print("--- Sector Limpieza ---")
    codigo = lector.leerCodigo(6002)  # detergente
    almacen.procesarEscaneo(codigo, carrito, cantidad=1)

    # PANADERIA - PROMO 20% DESCUENTO
    print("--- Sector Panaderia (Promo 20% descuento) ---")
    codigo = lector.leerCodigo(7001)  # pan lactal
    almacen.procesarEscaneo(codigo, carrito, cantidad=1)

    # PERFUMERIA
    print("--- Sector Perfumeria ---")
    codigo = lector.leerCodigo(8001)  # shampoo
    almacen.procesarEscaneo(codigo, carrito, cantidad=1)

    # VERDULERIA
    print("--- Sector Verduleria ---")
    codigo = lector.leerCodigo(9002)  # papa
    almacen.procesarEscaneo(codigo, carrito, cantidad=1)

    print("\n=== RESUMEN DE COMPRA ===")
    print(carrito)
    print("\n=== PAGO ===")
    cliente.pagar()
    