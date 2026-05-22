from tipos import prod_x_peso

class Carne(prod_x_peso):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso, tipo_corte : str, categoria : str):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso)
        self.__tipo_corte = tipo_corte
        self.__categoria = categoria

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Tipo de corte: {self.__tipo_corte} - Categoria: {self.__categoria}
        Precio por kilo: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Kilos disponibles: {self.getstock()}"""
        return texto_producto