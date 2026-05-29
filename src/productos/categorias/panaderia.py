from src.productos.tipos.prod_x_peso import Prod_x_peso

class Panaderia(Prod_x_peso):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, tipo_pan):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca)
        self.__tipo_pan = tipo_pan

    def __str__(self) -> str:
        texto_producto = f"""Producto: {self.getNombre()}
        Tipo de pan: {self.__tipo_pan} - Precio por kilo: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Kilos disponibles: {self.getStock()}"""
        return texto_producto

    def contar_bolsones (self) -> str: #tomamos como peso de un bolson 15 kilos
        bolsones = self.getStock() / 15
        return f"Hay {bolsones:.0f} bolsones sin abrir"