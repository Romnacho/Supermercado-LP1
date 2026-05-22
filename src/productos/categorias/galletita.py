from tipos import prod_x_unidad

class Galletita(prod_x_unidad):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete, sabor : str, pesoNeto : int, tieneTACC : bool):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__sabor = sabor
        self.__peso_neto = pesoNeto
        self.__tieneTACC = tieneTACC

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Sabor: {self.__sabor} - Tiene TACC: {'si' if self.__tieneTACC else 'no'}
        Unidades por paquete: {self.getunid_x_paquete} - Peso: {self.__peso_neto}
        Precio: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Unidades disponibles: {self.getstock()}"""
        return texto_producto