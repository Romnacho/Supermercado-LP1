from src.pedidos.pedido import Pedido

class Proveedor:
    def __init__(self, nombreEmpresa: str, cuit: int, mail: str, marcasQueProvee: list):
        self.__nombreEmpresa = nombreEmpresa
        self.__cuit = cuit
        self.__mail = mail
        self.__marcasQueProvee = marcasQueProvee
        self.__pedidosPendientes = []

    def agregarMarca(self, marca: str) -> None:
        self.__marcasQueProvee.append(marca)

    def recibirPedido(self, pedido: Pedido) -> None:
        self.__pedidosPendientes.append(pedido)

    def despacharMercaderia(self) -> None:
        for pedido in self.__pedidosPendientes:
            print(f"Despachando {pedido}")
        self.__pedidosPendientes = []

    def __str__(self):
        return f"{self.__nombreEmpresa} - CUIT: {self.__cuit} - Mail: {self.__mail} - Marca: {self.__marcaQueProvee}"