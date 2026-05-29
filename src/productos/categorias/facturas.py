from src.productos.tipos.prod_x_unidad import Prod_x_unidad

class Factura(Prod_x_unidad):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete, tipo):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__tipo = tipo

    def __str__(self):
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()}
        Tipo: {self.__tipo} - Unidades por paquete: {self.getUnid_X_Paquete()}
        Precio por unidad: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Paquetes disponibles: {self.getStock()}"""
        return texto_producto