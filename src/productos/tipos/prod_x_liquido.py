from productos.producto import Producto

class Prod_x_liquido(Producto):
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, cm3):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca)
        self.__cm3 = cm3

    def precioFinal(self, unidades_compradas):
        precio_final = self.getprecio() * unidades_compradas
        return precio_final
    
    def actualizarStock(self, stock_nuevo) -> None:
        self.stock += stock_nuevo
        return None
    
    def __str__():
        pass