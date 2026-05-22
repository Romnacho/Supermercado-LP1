from tipos import prod_x_liquido
#leche, yogurt, helado, cosas en cm3 q ves en una heladera
class Heladera(prod_x_liquido):
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, cm3, tipo : str): 
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, cm3)
        self.__tipo = tipo

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Tipo: {self.__tipo}
        Cm3: {self.getcm3()} - Precio: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Unidades disponibles: {self.getstock()}"""
        return texto_producto