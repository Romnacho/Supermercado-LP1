from productos.producto import Producto

class Prod_x_unidad(Producto):
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca)
        self.__unid_x_paquete = unid_x_paquete

    def precioFinal(self, unidades_compradas):
        precio_final = self.getprecio() * unidades_compradas
        return precio_final

    def __str__():
        pass 