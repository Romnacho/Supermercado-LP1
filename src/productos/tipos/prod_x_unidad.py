from producto import Producto

class Prod_x_unidad(Producto):
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, unid_x_paquete):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo)
        self.__unid_x_paquete = unid_x_paquete

    def precioFinal():
        pass

    def mostrarEnTablet():
        pass 