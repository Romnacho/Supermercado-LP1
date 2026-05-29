from src.productos.tipos.prod_x_unidad import Prod_x_unidad

class Galletita(Prod_x_unidad):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete, sabor, pesoNeto, tieneTACC):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__sabor = sabor
        self.__peso_neto = pesoNeto
        self.__tieneTACC = tieneTACC

    def __str__(self) -> str:
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()}
        Sabor: {self.__sabor} - TACC: {'Si' if self.__tieneTACC else 'No'}
        Unidades por paquete: {self.getUnid_X_Paquete()} - Peso: {self.__peso_neto}
        Precio por unidad: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Paquetes disponibles: {self.getStock()}"""
        return texto_producto