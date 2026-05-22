from tipos import prod_x_peso

class Verdura(prod_x_peso):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso, tipo_verdura : str):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso)
        self.__tipo_verdura = tipo_verdura

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Tipo de verdura: {self.__tipo_verdura} - Precio por kilo: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Kilos disponibles: {self.getstock()}"""
        return texto_producto