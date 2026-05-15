from src.productos.Producto import Producto

class Promocion:

    def __init__(self, tipo : int, cantidad_necesaria : int, productos_descontados : int, porcentaje_descuento : int):
        self.tipo = tipo
        self.cantidad_necesaria = cantidad_necesaria #cantidad de productos necesarios para aplicar el descuento, ej: 2*1, la cantidad necesaria es 2
        self.productos_descontados = productos_descontados #cantidad de productos descontados en promos como 2*1 o 3*2, en ambos casos los productos descontados son 1
        self.porcentaje_descuento = porcentaje_descuento

    def calcular_descuento(self, cantidad_comprada : int, producto : Producto):
        if self.tipo == 1:  #las promos de tipo uno son del tipo 2*1, 3*2, etc
            if cantidad_comprada == self.cantidad_necesaria:
                precio_final = producto.precio * (cantidad_productos - self.productos_descontados)