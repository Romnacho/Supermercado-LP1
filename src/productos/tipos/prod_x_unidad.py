from src.productos.producto import Producto

class Prod_x_unidad(Producto):
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca)
        self.__unid_x_paquete = unid_x_paquete

    def precioFinal(self):
        return self.__unid_x_paquete * self.getPrecio()
    
    def getUnid_X_Paquete(self):
        return self.__unid_x_paquete
    
  
        
    