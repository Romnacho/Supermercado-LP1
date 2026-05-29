from src.productos.producto import Producto

"""Clase hija de producto
representa a los productos que se venden por unidad como bebidar, galletitas, factuyras, etc"""

class Prod_x_unidad(Producto):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca)
        self.__unid_x_paquete = unid_x_paquete
        self.__tipo_producto = "Paquete"

    def precioFinal(self, cantidad : int = 1) -> float:
        return self.__unid_x_paquete * self.getPrecio() * cantidad
    
    """getters"""
    
    def getUnid_X_Paquete(self):
        return self.__unid_x_paquete
    
    def getTipoProducto(self):
        return self.__tipo_producto