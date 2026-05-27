class Deposito:
    def __init__(self, capacidadMax: int):
        self.__stockReserva = {}  #{codigoBarras: cantidad}
        self.__capacidadMax = capacidadMax

    def disponibilidad(self, codigo: int) -> int:
        return self.__stockReserva.get(codigo, 0)

    def reponer(self, codigo: int, cant: int) -> None:
        if codigo in self.__stockReserva:
            self.__stockReserva[codigo] -= cant

    def agregarStock(self, codigo: int, cant: int) -> None:
        if codigo in self.__stockReserva:
            self.__stockReserva[codigo] += cant
        else:
            self.__stockReserva[codigo] = cant

    def __str__(self):
        return f"Deposito - Capacidad max: {self.__capacidadMax} - Productos: {len(self.__stockReserva)}"