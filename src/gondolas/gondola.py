from src.hardware.tablet import Tablet
from src.hardware.sensor import Sensor
from src.productos import Producto
from typing import List

class Gondola:

    def __init__(self, idGondola : int, tipo: str, productos : List[Producto], sensores : List[Sensor], tablet : Tablet):
        self.__idGondola = idGondola
        self.__productos = productos
        self.sensores = sensores
        self.tablet = tablet
        self.__tipo = tipo

    def añadirProducto(self, producto) -> None:
        self.productos.append(producto)
        return
    
    def eliminarProducto(self, producto) -> None:
        self.productos.remove(producto)
        return
    
    def __str__(self):
        print (f"Gondola {self.__idGondola} - Tipo: {self.__tipo}")
        print ("Productos:")
        for producto in self.productos:
            print (producto.__str__())