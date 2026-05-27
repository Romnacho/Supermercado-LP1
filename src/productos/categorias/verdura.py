from src.productos.tipos.prod_x_peso import Prod_x_peso

class Verdura(Prod_x_peso):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso, tipo_verdura : str):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso)
        self.__tipo_verdura = tipo_verdura

    def __str__(self):
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()}
        Tipo de verdura: {self.__tipo_verdura} - Precio por kilo: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Kilos disponibles: {self.getStock()}"""
        return texto_producto