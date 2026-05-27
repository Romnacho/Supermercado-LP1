from src.almacen.deposito import Deposito
from src.pedidos.pedido import Pedido
from src.productos.producto import Producto

class Inventario:
    def __init__(self, capacidadMaxDeposito: int, umbralMinimoGlobal: int):
        self.__stockReserva = Deposito(capacidadMaxDeposito)
        self.__umbralMinimoGlobal = umbralMinimoGlobal

    def monitorearStock(self, producto : Producto) -> None:
        if producto.getStock() < producto.getUmbralMinimo():
            if self.__stockReserva.disponibilidad(producto.getCodigoBarras()) > 0:
                self.realizarReposicionInterna(producto)
            else:
                self.solicitarPedido(producto)

    def realizarReposicionInterna(self, producto : Producto) -> None:
        cantidad = self.__umbralMinimoGlobal - producto.getStock()
        self.__stockReserva.reponer(producto.getCodigoBarras(), cantidad)
        producto.actualizarStock(-cantidad)  #suma al stock del producto

    def solicitarPedido(self, producto : Producto) -> Pedido:
        pedido = Pedido(
            marca = producto.getMarca(),
            nombreProducto = producto.getNombre(),
            cantSolicitada = self.__umbralMinimoGlobal
        )
        return pedido

    def recibirPedido(self, pedido: Pedido) -> None:
        pedido.recibirPedido()
        self.__stockReserva.agregarStock(pedido.getNombreProducto(), pedido.getCantSolicitada())

    def __str__(self):
        return f"Inventario - Umbral minimo global: {self.__umbralMinimoGlobal}\n{self.__stockReserva}"