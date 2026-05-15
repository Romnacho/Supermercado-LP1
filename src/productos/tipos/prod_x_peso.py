from producto import Producto

class Prod_x_peso(Producto): 
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, peso):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo)
        self.__peso = peso
    
    def precioFinal():
        pass

    def actualizarStock(kg_vendidos):
        #actualiza, no devuelve nada
        return None
    
    def mostrarEnTablet():
        pass