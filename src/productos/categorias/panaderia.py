from tipos import prod_x_peso

class Panaderia(prod_x_peso):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso, tipo_pan : str):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, peso)
        self.__tipo_pan = tipo_pan

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()}
        Tipo de pan: {self.__tipo_pan} - Precio por kilo: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Kilos disponibles: {self.getstock()}"""
        return texto_producto

    def contar_bolsones (self) -> str:
        #tomamos como peso de un bolson 15 kilos
        bolsones = self.getstock() / 15
        return f"Hay {bolsones:.0f} bolsones sin abrir"