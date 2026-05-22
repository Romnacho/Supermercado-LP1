from productos.producto import Producto

class Prod_x_peso(Producto): 
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca)
        self.__peso = peso
        self.__precio_x_kilo = precio
    
    def precioFinal(self, kilos_comprados):
        precio_final = self.getprecio() * kilos_comprados
        return precio_final

    def actualizarStock(kg_vendidos):
        #actualiza, no devuelve nada
        return None
    
    def __str__():
        pass