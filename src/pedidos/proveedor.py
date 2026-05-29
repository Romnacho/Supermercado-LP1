from src.pedidos.pedido import Pedido

"""Recibe el pedido y te despacha la mercaderia"""

class Proveedor:
    def __init__(self, nombreEmpresa: str, cuit: int, mail: str, marcasQueProvee: list):
        self.__nombreEmpresa = nombreEmpresa
        self.__cuit = cuit
        self.__mail = mail
        self.__marcasQueProvee = marcasQueProvee
        self.__pedidosPendientes = []

    """Agrega una marca a las cosas q provee"""

    def agregarMarca(self, marca: str) -> None:
        self.__marcasQueProvee.append(marca)

    """Saca una marca de las cosas q provee"""

    def sacarMarca(self, marca: str) -> None:
        if marca in self.__marcasQueProvee:
            self.__marcasQueProvee.remove(marca)

    """Recibe un pedido y lo agrega a los pendientes"""

    def recibirPedido(self, pedido: Pedido) -> None:
        print("Pedido recibido")
        self.__pedidosPendientes.append(pedido)

    """Despacha la mercaderia"""

    def despacharMercaderia(self) -> None:
        print("Mercaderia despachada")
        for pedido in self.__pedidosPendientes:
            print(f"Despachando {pedido}")
        self.__pedidosPendientes = []
    
    """Retorna un texto que escribe informacion del proveedor"""

    def __str__(self):
        return f"{self.__nombreEmpresa} - CUIT: {self.__cuit} - Mail: {self.__mail} - Marca: {self.__marcaQueProvee}"