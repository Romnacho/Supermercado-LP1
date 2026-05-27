from src.hardware.lectordecodigo import LectorDeCodigoDeBarras
from src.hardware.pantallaOLED import PantallaOLED
from src.productos.producto import Producto

class Carrito:
    def __init__(self, lectorBarra: LectorDeCodigoDeBarras, pantalla: PantallaOLED):
        self.__listaProductos = []
        self.__lectorBarra = lectorBarra
        self.__pantalla = pantalla
        self.__totalAcumulado = 0.0

    def escanearYAgregar(self, producto: Producto) -> None:
        self.__listaProductos.append(producto)
        self.__totalAcumulado += producto.precioFinal()
        self.__pantalla.mostrarTotal(self.__totalAcumulado)

    def eliminarProducto(self, producto: Producto) -> None:
        if producto in self.__listaProductos:
            self.__listaProductos.remove(producto)
            self.__totalAcumulado -= producto.precioFinal()
            self.__pantalla.mostrarTotal(self.__totalAcumulado)

    def getTotalAcumulado(self) -> float:
        return self.__totalAcumulado

    def __str__(self):
        texto = "Carrito:\n"
        for producto in self.__listaProductos:
            texto += f"{producto}\n"
        texto += f"Total: ${self.__totalAcumulado}"
        return texto