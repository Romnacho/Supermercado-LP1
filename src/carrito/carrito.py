from src.hardware.lectordecodigo import LectorDeCodigoDeBarras
from src.hardware.pantallaOLED import PantallaOLED
from src.productos.producto import Producto

class Carrito:
    def __init__(self, lectorBarra: LectorDeCodigoDeBarras, pantalla: PantallaOLED):
        self.__listaProductos = [] #lista de tuplas (producto, precio)
        self.__lectorBarra = lectorBarra
        self.__pantalla = pantalla
        self.__totalAcumulado = 0.0

    def escanearYAgregar(self, producto: Producto, precio: float) -> None:
        self.__listaProductos.append((producto, precio))
        self.__totalAcumulado += precio
        self.__pantalla.mostrarTotal(self.__totalAcumulado)

    def eliminarProducto(self, producto: Producto, precio : float) -> None:
        if producto in self.__listaProductos:
            self.__listaProductos.remove((producto, precio))
            self.__totalAcumulado -= producto.precioFinal()
            self.__pantalla.mostrarTotal(self.__totalAcumulado)

    def vaciarCarrito(self) -> None:
        self.__listaProductos = []
        self.__totalAcumulado = 0.0
        self.__pantalla.mostrarTotal(self.__totalAcumulado)

    def getTotalAcumulado(self) -> float:
        return self.__totalAcumulado
    
    def getListaProductos(self):
        return self.__listaProductos

    def __str__(self):
        texto = "Carrito:\n"
        for producto, precio in self.__listaProductos:
            texto += f"{producto} - ${precio}\n"
        texto += f"Total: ${self.__totalAcumulado}"
        return texto