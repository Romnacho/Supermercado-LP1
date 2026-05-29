from src.productos.tipos.prod_x_unidad import Prod_x_unidad

class Limpieza(Prod_x_unidad):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete, tipoAplicacion, inflamable, toxico, pesoNeto):
        super().__init__(nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__tipoAplicacion = tipoAplicacion
        self.__inflamable = inflamable
        self.__toxico = toxico
        self.__pesoNeto = pesoNeto

    def __str__(self):
        texto_producto = f"""Producto: {self.getNombre()} - Marca: {self.getMarca()}
        Tipo de aplicacion: {self.__tipoAplicacion}
        Inflamable: {'Si' if self.__inflamable else 'No'} - Toxico: {'Si' if self.__toxico else 'No'}
        Peso: {self.__pesoNeto} - Precio por unidad: ${self.getPrecio()}
        Codigo de barras: {self.getCodigoBarras()} - Unidades disponibles: {self.getStock()}"""
        return texto_producto