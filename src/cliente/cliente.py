from src.carrito.carrito import Carrito

class Cliente:
    def __init__(self, idCliente: int, nombre: str, carrito: Carrito):
        self.__idCliente = idCliente
        self.__nombre = nombre
        self.__carrito = carrito

    """añade un producto al carrito, se llama desde el menu y llama al metodo de escanear y agregar"""

    def agarrarProducto(self, producto) -> None:
        self.__carrito.escanearYAgregar(producto)

    """Paga el total del carrito"""

    def pagar(self) -> float:
        total = self.__carrito.getTotalAcumulado()
        print(f"Total a pagar: ${total}")
        return total
    
    """Devuelve un str del cliente"""

    def __str__(self) -> str:
        return f"Cliente: {self.__nombre} - ID: {self.__idCliente}"