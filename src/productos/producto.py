class Producto:
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo):
        self._nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__codigoBarras = codigoBarras
        self.__umbralMinimo = umbralMinimo 
        pass

    @abs
    def precioFinal():
        #abc para cada hija
        pass

    def validarStock():
        #valida y devuelve bool
        return
    
    def actualizarPrecios(porcentaje):
        #actualiza el precio de todo por el porcentaje dado, no devuelve nada
        return None
    
    def getEtiquetaBase():
        #devuelve un str con los datos basicos del producto
        return
    
    @abs
    def mostrarEnTablet():
        #muestra en la tablet
        return None