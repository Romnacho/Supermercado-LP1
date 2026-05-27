from src.carrito.carrito import Carrito

class Cliente:
    def __init__(self, idCliente: int, nombre: str, carrito: Carrito):
        self.__idCliente = idCliente
        self.__nombre = nombre
        self.__carrito = carrito

    def agarrarProducto(self, producto) -> None:
        self.__carrito.escanearYAgregar(producto)

    def pagar(self) -> float:
        total = self.__carrito.getTotalAcumulado()
        print(f"Total a pagar: ${total}")
        return total

    def __str__(self):
        return f"Cliente: {self.__nombre} - ID: {self.__idCliente}"