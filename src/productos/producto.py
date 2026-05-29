from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio, stock, stockMax, codigoBarras, umbralMinimo, marca):
        self._nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__stockMax = stockMax
        self.__codigoBarras = codigoBarras
        self.__umbralMinimo = umbralMinimo 
        self.__marca = marca
        pass

    @abstractmethod
    def precioFinal(self): #calcula precio final
        pass

    """Valisa el stock, devuelve un booleano"""

    def validarStock(self) -> bool: #valida y devuelve bool
        return self.__stock > self.__umbralMinimo
    
    def actualizarPrecios(self, porcentaje: float) -> None: #actualiza el precio por el porcentaje dado, no devuelve nada
        self.__precio += self.__precio * (porcentaje/100)
        return None
    
    """Actualiza el stock, recibe la cantidad vendida y la resta"""

    def actualizarStock(self, vendido:float) -> None: #actualiza stock por cantidad vendida, no devuelve nada
        self.setStock(self.getStock() - vendido)
        return None
    
    """Getters y setters"""
    
    def getNombre(self):
        return self._nombre
    
    def getPrecio(self):
        return self.__precio

    def getStock(self):
        return self.__stock
    
    def getStockMaximo(self):
        return self.__stockMax
    
    def setStock(self, nuevo_stock):
        self.__stock = nuevo_stock
        return None

    def getCodigoBarras(self):
        return self.__codigoBarras
    
    def getUmbralMinimo(self):
        return self.__umbralMinimo
    
    def getMarca(self):
        return self.__marca
    