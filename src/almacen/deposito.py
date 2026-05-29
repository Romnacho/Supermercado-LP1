class Deposito:
    def __init__(self, capacidadMax: int):
        self.__stockReserva = {}  #{codigoBarras: cantidad}
        self.__capacidadMax = capacidadMax

    """Devuelve la disponibilidad de un producto"""

    def disponibilidad(self, codigo: int) -> int:
        return self.__stockReserva.get(codigo, 0)
    
    """Repone un producto, se llama al commprar, repone si es necesario"""

    def reponer(self, codigo: int, cant: int) -> None:
        if codigo in self.__stockReserva:
            self.__stockReserva[codigo] -= cant

    """Agrega stock al deposito, se llama dsp de recibir un pedido"""

    def agregarStock(self, codigo: int, cant: int) -> None:
        if codigo in self.__stockReserva:
            self.__stockReserva[codigo] += cant
        else:
            self.__stockReserva[codigo] = cant

    """Retorna un str del deposito"""

    def __str__(self):
        return f"Deposito - Capacidad max: {self.__capacidadMax} - Productos: {len(self.__stockReserva)}"