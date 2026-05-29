from src.productos.producto import Producto

class Promocion:

    """Clase encargada de calcular las promociones aplicables a un producto"""

    def __init__(self, tipo : int, cantidad_necesaria : int, productos_descontados : int, porcentaje_descuento : int):
        self.__tipo = tipo
        self.__cantidad_necesaria = cantidad_necesaria #cantidad de productos necesarios para aplicar el descuento, ej: 2*1, la cantidad necesaria es 2
        self.__productos_descontados = productos_descontados #cantidad de productos descontados en promos como 2*1 o 3*2, en ambos casos los productos descontados son 1
        self.__porcentaje_descuento = porcentaje_descuento

    """Metodo para aplicar la promocion a un producto, varia segun el tipo
    Tipo 1:Lleva X, paga Y, calcula la cantidad de productos que se descuentan segun la cantidad comprada
    Tipo 2: Descuento porcentual, aplica el descuento al precio final
    Tipo 3: Segunda unidad con descuento, mezcla los dos metodos anteriores, calcula las unidades que tienen descuento y aplica el descuento porcentual a esas unidades"""

    def aplicarPromo(self, cantidad_comprada: int, producto: Producto) -> float:
        precio_unitario = producto.precioFinal(1)  # precio de 1 paquete completo
        if self.__tipo == 1:
            grupos = cantidad_comprada // self.__cantidad_necesaria
            resto = cantidad_comprada % self.__cantidad_necesaria
            unidades_pagadas = grupos * (self.__cantidad_necesaria - self.__productos_descontados) + resto
            return precio_unitario * unidades_pagadas
        elif self.__tipo == 2:
            return precio_unitario * cantidad_comprada * (1 - self.__porcentaje_descuento / 100)
        elif self.__tipo == 3:
            pares = cantidad_comprada // 2
            resto = cantidad_comprada % 2
            precio_segunda = precio_unitario * (1 - self.__porcentaje_descuento / 100)
            return pares * (precio_unitario + precio_segunda) + resto * precio_unitario
        
    """Getter"""

    def getTipo(self) -> int:
        return self.__tipo
    
    """Metodo para representar la promocion como texto, varia segun el tipo"""

    def __str__(self) -> str:
        if self.__tipo == 1:
            return f"Llevá {self.__cantidad_necesaria} pagá {self.__cantidad_necesaria - self.__productos_descontados}"
        elif self.__tipo == 2:
            return f"{self.__porcentaje_descuento}% de descuento"
        elif self.__tipo == 3:
            return f"Segunda unidad {self.__porcentaje_descuento}% off"