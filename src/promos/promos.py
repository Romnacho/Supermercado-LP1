from src.productos.producto import Producto

class Promocion:

    def __init__(self, tipo : int, cantidad_necesaria : int, productos_descontados : int, porcentaje_descuento : int):
        self.__tipo = tipo
        self.__cantidad_necesaria = cantidad_necesaria #cantidad de productos necesarios para aplicar el descuento, ej: 2*1, la cantidad necesaria es 2
        self.__productos_descontados = productos_descontados #cantidad de productos descontados en promos como 2*1 o 3*2, en ambos casos los productos descontados son 1
        self.__porcentaje_descuento = porcentaje_descuento

    def aplicarPromo(self, cantidad_comprada: int, producto: Producto):
        precio_unitario = producto.precioFinal(1)  # precio de 1 paquete completo
        if self.__tipo == 1:
            if cantidad_comprada >= self.__cantidad_necesaria:
                return precio_unitario * (cantidad_comprada - self.__productos_descontados)
            return precio_unitario * cantidad_comprada
        elif self.__tipo == 2:
            return precio_unitario * cantidad_comprada * (1 - self.__porcentaje_descuento / 100)
        elif self.__tipo == 3:
            if cantidad_comprada >= 2:
                precio_segunda = precio_unitario * (1 - self.__porcentaje_descuento / 100)
                return precio_unitario + precio_segunda + precio_unitario * (cantidad_comprada - 2)
            return precio_unitario * cantidad_comprada
        
    def getTipo(self) -> int:
        return self.__tipo

    def __str__(self) -> str:
        if self.__tipo == 1:
            return f"Llevá {self.__cantidad_necesaria} pagá {self.__cantidad_necesaria - self.__productos_descontados}"
        elif self.__tipo == 2:
            return f"{self.__porcentaje_descuento}% de descuento"
        elif self.__tipo == 3:
            return f"Segunda unidad {self.__porcentaje_descuento}% off"