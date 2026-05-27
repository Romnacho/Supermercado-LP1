class Sensor:
    def __init__ (self, idSensor : int, estado : bool):
        self.__idSensor = idSensor
        self.__estado = estado

    def getId(self):
        return self.__idSensor

    def detectarStock(self):
        return self.__estado 