"""Imprime cosas"""
class Tablet:
    def __init__(self, idTablet : int):
        self.__idTablet = idTablet

    def mostrarInfoProducto(self, producto) -> None:
        print(producto)
        return None
    
    def mostrarPromos(self, promos) -> None:
        print(promos)
        return None
