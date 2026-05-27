from src.productos.producto import Producto

class Prod_x_unidad(Producto):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca)
        self.__unid_x_paquete = unid_x_paquete

    def precioFinal(self, cantidad : int = 1):
        return self.__unid_x_paquete * self.getPrecio() * cantidad
    
    def getUnid_X_Paquete(self):
        return self.__unid_x_paquete
    
  
        
    