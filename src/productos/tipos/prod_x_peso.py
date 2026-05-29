from src.productos.producto import Producto

"""Hija de la clase Producto
Representa a los productos que se vender por peso como verdura, fiambre, etc"""

class Prod_x_peso(Producto): 
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca)
        self.__tipo_producto = "Peso"

    """Metodo para calucular el precio final de un producto
    recibe los kilos comprados y devuelve el precio final"""

    def precioFinal(self, kilos_comprados : float = 1) -> float: 
        return self.getPrecio() * kilos_comprados
    
    def getTipoProducto(self):
        return self.__tipo_producto