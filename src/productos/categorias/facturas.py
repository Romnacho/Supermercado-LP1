from tipos import prod_x_unidad

class Factura(prod_x_unidad):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete, tipo : str):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__tipo = tipo

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Tipo: {self.__tipo} - Unidades por paquete: {self.getunid_x_paquete}
        Precio: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Unidades disponibles: {self.getstock()}"""
        return texto_producto