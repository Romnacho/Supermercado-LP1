from tipos import prod_x_unidad

class Limpieza(prod_x_unidad):

    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete, tipoAplicacion : str, inflamable : bool, toxico : bool, pesoNeto : int):
        super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete)
        self.__tipoAplicacion = tipoAplicacion
        self.__inflamable = inflamable
        self.__toxico = toxico
        self.__pesoNeto = pesoNeto

    def __str__(self):
        texto_producto = f"""Producto: {self.getnombre()} - Marca: {self.getmarca()}
        Tipo de aplicacion: {self.__tipoAplicacion}
        Inflamable: {'si' if self.__inflamable else 'no'} - Toxico: {'si' if self.__toxico else 'no'}
        Unidades por paquete: {self.getunid_x_paquete} - Peso: {self.__pesoNeto}
        Precio: ${self.getprecio()}
        Codigo de barras: {self.getcodigoBarras()} - Unidades disponibles: {self.getstock()}"""
        return texto_producto