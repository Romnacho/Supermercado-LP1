from src.productos.producto import Producto

class Prod_x_peso(Producto): 
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca)
    
    def precioFinal(self, kilos_comprados): 
        return self.getPrecio() * kilos_comprados
    
 
    