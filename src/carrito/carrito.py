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
        for (producto_aux, precio_aux, cantidad_aux) in self.__listaProductos:
            if producto.getCodigoBarras() == producto_aux.getCodigoBarras():
                nuevo_precio = precio_aux + precio
                nueva_cantidad = cantidad_aux + cantidad
                self.__listaProductos.remove((producto_aux, precio_aux, cantidad_aux))
                self.__listaProductos.append((producto_aux, nuevo_precio, nueva_cantidad))
                self.__totalAcumulado += precio
                self.__pantalla.mostrarTotal(self.__totalAcumulado)
                return
        self.__listaProductos.append((producto, precio, cantidad))
        self.__totalAcumulado += precio
        self.__pantalla.mostrarTotal(self.__totalAcumulado)
        return

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