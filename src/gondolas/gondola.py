from src.hardware.tablet import Tablet
from src.hardware.sensor import Sensor
from src.productos.producto import Producto
from src.productos.tipos.prod_x_peso import Prod_x_peso
from src.productos.tipos.prod_x_unidad import Prod_x_unidad
from src.productos.categorias.bebidas import Bebidas
from src.productos.categorias.fiambre import Fiambre
from src.productos.categorias.verdura import Verdura
from src.productos.categorias.carne import Carne
from src.productos.categorias.facturas import Factura
from src.productos.categorias.galletita import Galletita
from src.productos.categorias.limpieza import Limpieza
from src.productos.categorias.perfumeria import Perfumeria
from src.productos.categorias.panaderia import Panaderia
from typing import List

class Gondola:

    def __init__(self, idGondola : int, tipo: str, productos : List[Producto], sensores : List[Sensor], tablet : Tablet):
        self.__idGondola = idGondola
        self.__productos = productos
        self.sensores = sensores
        self.tablet = tablet
        self.__tipo = tipo

    def añadirProducto(self, producto) -> None:
        self.__productos.append(producto)
        return
    
    def eliminarProducto(self, producto) -> None:
        self.__productos.remove(producto)
        return
    
    def __str__(self):
        print (f"Gondola {self.__idGondola} - Tipo: {self.__tipo}")
        print ("Productos:")
        for producto in self.__productos:
            print (producto.__str__())