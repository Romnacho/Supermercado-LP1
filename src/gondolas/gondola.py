from src.hardware.tablet import Tablet
from src.hardware.sensor import Sensor
from src.productos import Producto
from typing import List

class Gondola:

    def __init__(self, idGondola : int, productos : List[Producto], sensores : List[Sensor], tablet : Tablet):
        self.idGondola = idGondola
        self.productos = productos
        self.sensores = sensores
        self.tablet = tablet