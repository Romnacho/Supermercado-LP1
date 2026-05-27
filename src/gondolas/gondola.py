from src.hardware.tablet import Tablet
from src.hardware.sensor import Sensor
from src.productos.producto import Producto
from typing import List

class Gondola():
    def __init__(self, idGondola : int, tipo: str, productos : List[Producto], sensores : List[Sensor], tablet : Tablet, promo : int):
        self.__idGondola = idGondola
        self.__productos = productos
        self.__sensores = sensores
        self.__tablet = tablet
        self.__tipo = tipo
        self.__promo = promo #None si no tiene promos, sino, el numero de promo

    def añadirProducto(self, producto) -> None:
        self.__productos.append(producto)
        return
    
    def eliminarProducto(self, producto) -> None:
        self.__productos.remove(producto)
        return
    
    def mostrarTablet(self) -> None:
        for producto in self.__productos:
            self.__tablet.mostrarInfoProducto(producto)
    
    def mostrarPromociones(self) -> None:
        if self.__promo:
            self.__tablet.mostrarPromos(self.__promo)
        else:
            print("Esta góndola no tiene promociones")
    
    def __str__(self):
        texto = f"Gondola {self.__idGondola} - Tipo: {self.__tipo}\nProductos:\n"
        for producto in self.__productos:
            texto += f"{producto}\n"
        return texto