from tipos import prod_x_peso

class Fiambre(prod_x_peso):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso, tipo_fiambre : str):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso)
        self.__tipo_fiambre = tipo_fiambre

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Tipo de fiambre: {self.__tipo_fiambre} - Precio por kilo: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Kilos disponibles: {self.getstock()}"""
        return texto_producto
    
    #def contar_fetas (self)
    #No se para q sea pero esta en el uml