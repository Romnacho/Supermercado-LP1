from src.productos.tipos.prod_x_peso import Prod_x_peso

class Panaderia(Prod_x_peso):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, tipo_pan):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca)
        self.__tipo_pan = tipo_pan

    def __str__(self) -> str:
        texto_producto = f"""Producto: {self.getNombre()}
        Tipo de pan: {self.__tipo_pan} - Precio por kilo: ${self.getPrecio()} - Kilo por bolson: 3
        Codigo de barras: {self.getCodigoBarras()} - Bolsones disponibles: {self.contar_bolsones():.2f}"""
        return texto_producto

    def contar_bolsones (self) -> str: #tomamos como peso de un bolson 3 kilos
        bolsones = self.getStock() / 3
        return bolsones