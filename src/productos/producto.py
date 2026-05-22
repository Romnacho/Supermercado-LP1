class Producto:
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca):
        self._nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__codigoBarras = codigoBarras
        self.__umbralMinimo = umbralMinimo 
        self.__marca = marca
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
    def __str__():
        #muestra en la tablet
        return None