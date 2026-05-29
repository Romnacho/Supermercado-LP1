from src.productos.tipos.prod_x_peso import Prod_x_peso

class Fiambre(Prod_x_peso):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, tipo_fiambre):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca)
        self.__tipo_fiambre = tipo_fiambre

    def __str__(self) -> str:
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()}
        Tipo de fiambre: {self.__tipo_fiambre} - Precio por kilo: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Kilos disponibles: {self.getStock()}"""
        return texto_producto
    
    #def contar_fetas (self)
    #No se para q sea pero esta en el uml