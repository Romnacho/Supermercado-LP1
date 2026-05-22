from tipos import prod_x_liquido

class Perfumeria(prod_x_liquido):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, cm3, fragancia : str, importado : bool):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca,cm3)
        self.__fragancia = fragancia
        self.__importado = importado

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Fragancia: {self.__fragancia} - Importado: {'Si' if self.__importado else 'No'}
        Cm3: {self.getcm3()} - Precio: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Unidades disponibles: {self.getstock()}"""
        return texto_producto
    