from src.gondola.gondola import Gondola
from src.almacen.inventario import Inventario
from src.productos.producto import Producto
from src.carrito.carrito import Carrito
from src.promos.promos import Promocion
from src.pedidos.pedido import Pedido
from src.pedidos.proveedor import Proveedor
from typing import List, Union

class Almacen:
    def __init__(self, listaGondolas: List[Gondola], inventario: Inventario, promos: list[Promocion], proveedor : Proveedor):
        self.__listaGondolas = listaGondolas
        self.__inventario = inventario
        self.__preciosXCodigo = {}  #{codigoBarras: producto}
        self.__promos = promos
        self.__proveedor = proveedor

    """Registra un producto al sistema"""

    def registrarProducto(self, producto: Producto) -> None:
        self.__preciosXCodigo[producto.getCodigoBarras()] = producto

    """Procesa el escaneo de un producto, actualiza el carrito, el stock y gestiona la reposicion si es necesario"""

    def procesarEscaneo(self, codigo: int, carrito: Carrito, cantidad: int = 1) -> Union[Pedido, bool, None]:
        producto = self.__preciosXCodigo.get(codigo)
        if producto:
            if producto.getStock() < cantidad:
                print(f"\nStock insuficiente. Solo hay {producto.getStock()} unidades de {producto.getNombre()}")
                return False
            precio_final = self.calcularPrecioFinal(producto, cantidad)
            carrito.escanearYAgregar(producto, precio_final, cantidad)
            producto.actualizarStock(cantidad)
            return self.gestionarReposicion(producto)  # genera pedido si hace falta
        else:
            print(f"Producto con codigo {codigo} no encontrado")
            return False
        
    """Gestiona la reposicion de un producto, se llama al comprar, repone o genera el pedido si es necesario"""

    def gestionarReposicion(self, producto: Producto):
        print(f"\nCheckeando stock de {producto.getNombre()}")
        if producto.getStock() < producto.getUmbralMinimo():
            cantidad_necesaria = producto.getStockMaximo() - producto.getStock()
            disponible = self.__inventario.getDisponibilidad(producto.getCodigoBarras())
            cantidad_a_reponer = min(cantidad_necesaria, disponible)
            if cantidad_a_reponer > 0:
                producto.actualizarStock(-cantidad_a_reponer)
                self.__inventario.restarDelDeposito(producto.getCodigoBarras(), cantidad_a_reponer)
            pedido = self.__inventario.monitorearStock(producto)
            if pedido:
                print("\nStock bajo, contactando proveedor...")
                self.__proveedor.recibirPedido(pedido)
                self.__proveedor.despacharMercaderia()
                self.__inventario.recibirPedido(pedido)
                self.reponerProducto(pedido.getCodigoBarras())
            return None
        print("Stock OK")
        return None
    
    """Repone un producto, se llama dso de recibir un pedido, repone desde deposito sin generar pedido"""

    def reponerProducto(self, codigo: int):
        # se llama despues de recibir pedido, solo repone sin generar pedido
        producto = self.__preciosXCodigo.get(codigo)
        print(f"Stock actual: {producto.getStock()} - Umbral: {producto.getUmbralMinimo()}")
        print(f"Disponible en deposito: {self.__inventario.getDisponibilidad(codigo)}")
        if producto:
            if producto.getStock() < producto.getUmbralMinimo():
                cantidad_necesaria = producto.getStockMaximo() - producto.getStock()
                disponible = self.__inventario.getDisponibilidad(codigo)
                cantidad_a_reponer = min(cantidad_necesaria, disponible)
                if cantidad_a_reponer > 0:
                    producto.actualizarStock(-cantidad_a_reponer)
                    self.__inventario.restarDelDeposito(codigo, cantidad_a_reponer)
                    print(f"Stock de {producto.getNombre()} repuesto a {producto.getStock()}")
        return None

    """Calcula el precio final y aplica las promos si corresponden"""

    def calcularPrecioFinal(self, producto: Producto, cantidad: int) -> float:
        gondola = self.__buscarGondola(producto)
        if gondola and gondola.getPromo() != 0:
            tipo_promo = gondola.getPromo()
            promo = next((p for p in self.__promos if p.getTipo() == tipo_promo), None)
            if promo:
                precio_sin_promo = producto.precioFinal(cantidad)
                precio_con_promo = promo.aplicarPromo(cantidad, producto)
                ahorro = precio_sin_promo - precio_con_promo
                if ahorro > 0:
                    print(f"\n🏷️  Promo aplicada: {promo}")
                    print(f"   Precio sin promo: ${precio_sin_promo}")
                    print(f"   Precio con promo: ${precio_con_promo}")
                    print(f"   Ahorro: ${ahorro}")
                return precio_con_promo
        return producto.precioFinal(cantidad)
    
    """Getter"""

    def getListaGondolas(self) -> List[Gondola]:
        return self.__listaGondolas
    
    """Busca una gondola por un producto"""

    def __buscarGondola(self, producto: Producto) -> Gondola:
        for gondola in self.__listaGondolas:
            if gondola.tieneProducto(producto):
                return gondola
        return None
    
    """Imprime las gondolas"""

    def __str__(self):
        return f"Almacen - Gondolas: {len(self.__listaGondolas)}"