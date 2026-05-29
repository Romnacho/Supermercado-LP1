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
        self.__promo = promo #0 si no tiene promos, sino, el numero de promo

    """Añade un produto nuevo a la gondola"""

    def añadirProducto(self, producto) -> None:
        self.__productos.append(producto)
        return
    
    """Borra un producto de la gondola"""
    
    def eliminarProducto(self, producto) -> None:
        self.__productos.remove(producto)
        return
    
    """Muestra la info de los producots en la tablet"""
    
    def mostrarTablet(self) -> None:
        for producto in self.__productos:
            self.__tablet.mostrarInfoProducto(producto)

    """Muestra las promos"""
    
    def mostrarPromociones(self) -> None:
        if self.__promo:
            self.__tablet.mostrarPromos(self.__promo)
        else:
            print("Esta góndola no tiene promociones")

    """Getters"""

    def getPromo(self):
        return self.__promo
    
    def getTipo(self) -> str:
        return self.__tipo
    
    def getPromoDescripcion(self) -> str:
        if self.__promo == 1:
            return "2x1"
        elif self.__promo == 2:
            return "20% de descuento"
        elif self.__promo == 3:
            return "Segunda unidad 50% off"
        return ""

    def getProductos(self) -> list:
        return self.__productos
    
    """Detecta si estan los productos en la gondola"""
    
    def tieneProducto(self, producto: Producto) -> bool:
        return producto in self.__productos and any(sensor.detectarStock() for sensor in self.__sensores)
    
    """Representa la gondola como texto"""
    
    def __str__(self):
        texto = f"Gondola {self.__idGondola} - Tipo: {self.__tipo}\nProductos:\n"
        for producto in self.__productos:
            texto += f"{producto}\n"
        return texto