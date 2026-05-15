from producto import Producto

class Prod_x_liquido(Producto):
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, cm3):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo)
        self.__cm3 = cm3

    def precioFinal():
        #aca se sobreescribe el metodo padre, todo
        return
    
    def actualizarStock(cm3_vendidos):
        #actualiza, no devuelve nada
        return None
    
    def mostrarEnTablet():
        pass