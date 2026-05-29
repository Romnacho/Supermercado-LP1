"""Representa los pedidos realizados por el supermercado a los proveedores, suceden cuando el stock de un producto es menor al umbal minimo"""

class Pedido:
    __contador = 0 #para id
    def __init__(self, marca: str, nombreProducto: str, cantSolicitada: float, codigoBarras):
        Pedido.__contador += 1
        self.__idPedido = Pedido.__contador
        self.__marca = marca
        self.__nombreProducto = nombreProducto
        self.__cantSolicitada = cantSolicitada
        self.__codigoBarras = codigoBarras
        self.__estado = "pendiente"

    """Metodo que marca el pedido como recibido"""

    def recibirPedido(self) -> None:
        self.__estado = "recibido"

    """Metodo para consultar el estado del pedido"""

    def estadoPedido(self) -> str:
        return self.__estado
    
    """Getters"""
    
    def getCantSolicitada(self) -> float:
        return self.__cantSolicitada
    
    def getNombreProducto(self) -> str:
        return self.__nombreProducto

    def getMarca(self) -> str:
        return self.__marca
    
    def getCodigoBarras(self) -> int:
        return self.__codigoBarras
    
    """Retorna un texto que representa al pedido"""

    def __str__(self) -> str:
        return f"Pedido {self.__idPedido} - {self.__nombreProducto} ({self.__marca}) - Cantidad: {self.__cantSolicitada} - Estado: {self.__estado}"