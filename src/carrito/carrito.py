from src.hardware.lectordecodigo import LectorDeCodigoDeBarras
from src.hardware.pantallaOLED import PantallaOLED
from src.productos.producto import Producto

class Carrito:
    def __init__(self, lectorBarra: LectorDeCodigoDeBarras, pantalla: PantallaOLED):
        self.__listaProductos = [] #lista de tuplas (producto, precio)
        self.__lectorBarra = lectorBarra
        self.__pantalla = pantalla
        self.__totalAcumulado = 0.0

    """Escanea un producto, lo agrega al carrito y va sumando el precio final"""

    def escanearYAgregar(self, producto: Producto, precio: float, cantidad: float) -> None:
        self.__listaProductos.append((producto, precio, cantidad))
        self.__totalAcumulado += precio
        self.__pantalla.mostrarTotal(self.__totalAcumulado)

    """Elimina productos del carrito y baja el precio final"""

    def eliminarProducto(self, producto: Producto, precio : float, cantidad : float) -> None:
        if (producto, precio, cantidad) in self.__listaProductos:
            self.__listaProductos.remove((producto, precio, cantidad))
            self.__totalAcumulado -= precio
            self.__pantalla.mostrarTotal(self.__totalAcumulado)

    """Vacia el carrito"""

    def vaciarCarrito(self) -> None:
        self.__listaProductos = []
        self.__totalAcumulado = 0.0
        self.__pantalla.mostrarTotal(self.__totalAcumulado)

    """Getters"""

    def getTotalAcumulado(self) -> float:
        return self.__totalAcumulado
    
    def getListaProductos(self) -> list:
        return self.__listaProductos
    
    """Decuelce un str del carrito"""

    def __str__(self) -> str:
        texto = "Carrito:\n"
        for producto, precio, cantidad in self.__listaProductos:
            texto += f"{producto} - ${precio}\n"
        texto += f"Total: ${self.__totalAcumulado}"
        return texto