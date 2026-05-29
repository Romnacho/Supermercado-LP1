from src.productos.tipos.prod_x_unidad import Prod_x_unidad

class Perfumeria(Prod_x_unidad):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete, cm3, fragancia, importado):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__cm3 = cm3
        self.__fragancia = fragancia
        self.__importado = importado

    def __str__(self):
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()}
        Fragancia: {self.__fragancia} - Importado: {'Si' if self.__importado else 'No'}
        Cm3: {self.__cm3} - Precio por unidad: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Unidades disponibles: {self.getStock()}"""
        return texto_producto
    