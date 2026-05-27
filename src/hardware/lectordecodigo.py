class LectorDeCodigoDeBarras :
    def __init__(self, idLector):
        self.__idLector = idLector
        pass

    def leerCodigo(self, codigo):
        return codigo

    def enviarAlCarrito(self, carrito, codigo):
        carrito.escanearYAgregar(codigo)