from src.gondola.gondola import Gondola
from src.almacen.inventario import Inventario
from src.productos.producto import Producto
from src.carrito.carrito import Carrito
from src.promos.promos import Promocion
from typing import List

class Almacen:
    def __init__(self, listaGondolas: List[Gondola], inventario: Inventario, promos: list[Promocion]):
        self.__listaGondolas = listaGondolas
        self.__inventario = inventario
        self.__preciosXCodigo = {}  #{codigoBarras: producto}
        self.__promos = promos

    def registrarProducto(self, producto: Producto) -> None:
        self.__preciosXCodigo[producto.getCodigoBarras()] = producto

    def procesarEscaneo(self, codigo: int, carrito: Carrito, cantidad: int = 1):
        producto = self.__preciosXCodigo.get(codigo)
        if producto:
            if producto.getStock() < cantidad:
                print(f"\nStock insuficiente. Solo hay {producto.getStock()} unidades de {producto.getNombre()}")
                return False
            precio_final = self.calcularPrecioFinal(producto, cantidad)
            carrito.escanearYAgregar(producto, precio_final)
            producto.actualizarStock(cantidad)
            return self.gestionarReposicion(producto)  # genera pedido si hace falta
        else:
            print(f"Producto con codigo {codigo} no encontrado")
            return False

    def gestionarReposicion(self, producto: Producto):
        # se llama al comprar, repone desde deposito o genera pedido
        print(f"\nCheckeando stock de {producto.getNombre()}")
        if producto.getStock() < producto.getUmbralMinimo():
            cantidad_necesaria = producto.getStockMaximo() - producto.getStock()
            disponible = self.__inventario.getDisponibilidad(producto.getCodigoBarras())
            cantidad_a_reponer = min(cantidad_necesaria, disponible)
            if cantidad_a_reponer > 0:
                producto.actualizarStock(-cantidad_a_reponer)
                self.__inventario.restarDelDeposito(producto.getCodigoBarras(), cantidad_a_reponer)
            return self.__inventario.monitorearStock(producto)  # genera pedido si deposito vacio
        print("Stock OK")
        return None

    def reponerProducto(self, codigo: int):
        # se llama despues de recibir pedido, solo repone sin generar pedido
        producto = self.__preciosXCodigo.get(codigo)
        print(f"Stock actual: {producto.getStock()} - Umbral: {producto.getUmbralMinimo()}")
        print(f"Disponible en deposito: {self.__inventario.getDisponibilidad(codigo)}")
        if producto:
            if producto.getStock() < producto.getUmbralMinimo():
                cantidad_necesaria = producto.getStockMaximo() - producto.getStock()
                disponible = self.__inventario.getDisponibilidad(codigo)
                cantidad_a_reponer = min(cantidad_necesaria, disponible)
                if cantidad_a_reponer > 0:
                    producto.actualizarStock(-cantidad_a_reponer)
                    self.__inventario.restarDelDeposito(codigo, cantidad_a_reponer)
                    print(f"Stock de {producto.getNombre()} repuesto a {producto.getStock()}")
        return None

    def calcularPrecioFinal(self, producto: Producto, cantidad: int) -> float:
        gondola = self.__buscarGondola(producto)
        if gondola and gondola.getPromo() != 0:
            tipo_promo = gondola.getPromo()
            promo = next((p for p in self.__promos if p.getTipo() == tipo_promo), None)
            if promo:
                precio_sin_promo = producto.precioFinal(cantidad)
                precio_con_promo = promo.aplicarPromo(cantidad, producto)
                ahorro = precio_sin_promo - precio_con_promo
                if ahorro > 0:
                    print(f"\n🏷️  Promo aplicada: {promo}")
                    print(f"   Precio sin promo: ${precio_sin_promo}")
                    print(f"   Precio con promo: ${precio_con_promo}")
                    print(f"   Ahorro: ${ahorro}")
                return precio_con_promo
        return producto.precioFinal(cantidad)

    def getListaGondolas(self):
        return self.__listaGondolas

    def __buscarGondola(self, producto: Producto) -> Gondola:
        for gondola in self.__listaGondolas:
            if gondola.tieneProducto(producto):
                return gondola
        return None

    def __str__(self):
        return f"Almacen - Gondolas: {len(self.__listaGondolas)}"