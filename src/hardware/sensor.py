"""devuelve la situacion de un producto en cuanto al stock"""

class Sensor:
    def __init__ (self, idSensor : int, estado : bool):
        self.__idSensor = idSensor
        self.__estado = estado

    def getId(self) -> int:
        return self.__idSensor

    def detectarStock(self) -> bool:
        return self.__estado 