from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca):
        self._nombre = nombre
        self.__precio = precio
        self.__stock = stock
        self.__codigoBarras = codigoBarras
        self.__umbralMinimo = umbralMinimo 
        self.__marca = marca
        pass

    @abstractmethod
    def precioFinal(self): #calcula precio final
        pass

    def validarStock(self): #valida y devuelve bool
        return self.__stock > self.__umbralMinimo
    
    def actualizarPrecios(self, porcentaje): #actualiza el precio por el porcentaje dado, no devuelve nada
        self.__precio += self.__precio * (porcentaje/100)
        return None

    def actualizarStock(self, vendido): #actualiza stock por cantidad vendida, no devuelve nada
        self.setStock(self.getStock() - vendido)
        return None
    
    def getNombre(self):
        return self._nombre
    
    def getPrecio(self):
        return self.__precio

    def getStock(self):
        return self.__stock
    
    def setStock(self, nuevo_stock):
        self.__stock = nuevo_stock
        return None

    def getCodigoBarras(self):
        return self.__codigoBarras
    
    def getUmbralMinimo(self):
        return self.__umbralMinimo
    
    def getMarca(self):
        return self.__marca
    