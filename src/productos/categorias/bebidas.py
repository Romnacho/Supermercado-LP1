from src.productos.tipos.prod_x_unidad import Prod_x_unidad

class Bebidas(Prod_x_unidad):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete, cm3, sabor, porcentajeAlcohol):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__cm3 = cm3
        self.__sabor = sabor
        self.__porcentajeAlcohol = porcentajeAlcohol

    def __str__(self):
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()} -
        Sabor: {self.__sabor} - Porcentaje de alcohol: {self.__porcentajeAlcohol}% -
        Cm3: {self.__cm3} - Precio: ${self.getPrecio()} -
        Codigo de barras: {self.getCodigoBarras()} - Unidades disponibles: {self.getStock()}"""
        return texto_producto