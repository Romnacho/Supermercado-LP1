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

    def procesarEscaneo(self, codigo: int, carrito: Carrito, cantidad: int = 1) -> None:
        producto = self.__preciosXCodigo.get(codigo)
        if producto:
            precio_final = self.calcularPrecioFinal(producto, cantidad)
            carrito.escanearYAgregar(producto, precio_final)
            self.gestionarReposicion(producto)
        else:
            print(f"Producto con codigo {codigo} no encontrado")

    def calcularPrecioFinal(self, producto: Producto, cantidad: int) -> float:
        gondola = self.__buscarGondola(producto)
        if gondola and gondola.getPromo() != 0:
            tipo_promo = gondola.getPromo()
            promo = next((p for p in self.__promos if p.getTipo() == tipo_promo), None)
            if promo:
                return promo.aplicarPromo(cantidad, producto)
        return producto.precioFinal() * cantidad

    def gestionarReposicion(self, producto: Producto) -> None:
        if producto.getStock() < producto.getUmbralMinimo():
            cantidad_necesaria = producto.getStockMaximo() - producto.getStock()
            disponible = self.__inventario.getDisponibilidad(producto.getCodigoBarras())
            cantidad_a_reponer = min(cantidad_necesaria, disponible)
            producto.actualizarStock(-cantidad_a_reponer)
            self.__inventario.monitorearStock(producto)

    def __buscarGondola(self, producto: Producto) -> Gondola:
        for gondola in self.__listaGondolas:
            if gondola.tieneProducto(producto):
                return gondola
        return None

    def __str__(self):
        return f"Almacen - Gondolas: {len(self.__listaGondolas)}"