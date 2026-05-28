from src.almacen.deposito import Deposito
from src.pedidos.pedido import Pedido
from src.productos.producto import Producto

class Inventario:
    def __init__(self, capacidadMaxDeposito: int, umbralMinimoGlobal: int, cantPedido : int):
        self.__stockReserva = Deposito(capacidadMaxDeposito)
        self.__umbralMinimoGlobal = umbralMinimoGlobal
        self.__cantidadPedido = cantPedido

    def monitorearStock(self, producto: Producto) -> None:
        if producto.getStock() < producto.getUmbralMinimo():
            print("Stock bajo, checkeando deposito")
            if self.__stockReserva.disponibilidad(producto.getCodigoBarras()) > 0:
                self.realizarReposicionInterna(producto)
            else:
                return self.solicitarPedido(producto)
        if self.__stockReserva.disponibilidad(producto.getCodigoBarras()) < self.__umbralMinimoGlobal: #chequea si el deposito global esta bajo
            return self.solicitarPedido(producto)
        return None
    
    def realizarReposicionInterna(self, producto: Producto) -> None:
        print("Reponiendo desde deposito")
        cantidad_necesaria = producto.getStockMaximo() - producto.getStock()
        disponible = self.__stockReserva.disponibilidad(producto.getCodigoBarras())
        cantidad_a_reponer = min(cantidad_necesaria, disponible)
        self.__stockReserva.reponer(producto.getCodigoBarras(), cantidad_a_reponer)
        producto.actualizarStock(-cantidad_a_reponer)  #suma al stock del producto

    def solicitarPedido(self, producto: Producto) -> Pedido:
        print("Solicitando pedido del producto a Proveedor")
        pedido = Pedido(
        marca=producto.getMarca(),
        nombreProducto=producto.getNombre(),
        cantSolicitada=producto.getStockMaximo() + self.__cantidadPedido,
        codigoBarras=producto.getCodigoBarras()
        )
        return pedido

    def recibirPedido(self, pedido: Pedido) -> None:
        print("Pedido recibido, acutalizando stock")
        pedido.recibirPedido()
        self.__stockReserva.agregarStock(pedido.getCodigoBarras(), pedido.getCantSolicitada())

    def restarDelDeposito(self, codigoBarras: int, cantidad: int) -> None:
        self.__stockReserva.reponer(codigoBarras, cantidad)

    def getDisponibilidad(self, codigoBarras: int) -> int:
        return self.__stockReserva.disponibilidad(codigoBarras)
    
    def getDeposito(self):
        return self.__stockReserva

    def __str__(self):
        return f"Inventario - Umbral minimo global: {self.__umbralMinimoGlobal}\n{self.__stockReserva}"