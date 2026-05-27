class Pedido:
    def __init__(self, idPedido: int, marca: str, nombreProducto: str, cantSolicitada: float):
        self.__idPedido = idPedido
        self.__marca = marca
        self.__nombreProducto = nombreProducto
        self.__cantSolicitada = cantSolicitada
        self.__estado = "pendiente"

    def recibirPedido(self) -> None:
        self.__estado = "recibido"

    def estadoPedido(self) -> str:
        return self.__estado
    
    def getCantSolicitada(self) -> float:
        return self.__cantSolicitada
    
    def getNombreProducto(self) -> str:
        return self.__nombreProducto

    def getMarca(self) -> str:
        return self.__marca

    def __str__(self):
        return f"Pedido {self.__idPedido} - {self.__nombreProducto} ({self.__marca}) - Cantidad: {self.__cantSolicitada} - Estado: {self.__estado}"