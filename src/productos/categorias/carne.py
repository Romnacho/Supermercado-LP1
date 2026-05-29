from src.productos.tipos.prod_x_peso import Prod_x_peso

class Carne(Prod_x_peso):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, tipo_corte, categoria):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca)
        self.__tipo_corte = tipo_corte
        self.__categoria = categoria

    def __str__(self) -> str:
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()}
        Tipo de corte: {self.__tipo_corte} - Categoria: {self.__categoria}
        Precio por kilo: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Kilos disponibles: {self.getStock():.2f}"""
        return texto_producto