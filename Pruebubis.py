from src.gondolas.gondola import Gondola
from src.productos import *
from src.productos.categorias.galletita import Galletitas

#(self, nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete, sabor : str, pesoNeto : int, tieneTACC : bool):
 #       super().__init__(nombre, precio, stock, codigoBarras, umbralMinimo, marca, unid_x_paquete)

sonrisas = Galletitas("Sonrisas", 3000, 10, "123456789", 5, "Bagley", 12, "Sonrisas", 260, True)
pitusas_frutilla = Galletitas("Pitusas de frutilla", 2000, 15, "987654321", 5, "ParNor", 6, "Frutilla", 200, True)
oreos = Galletitas("Oreos", 2500, 20, "111222333", 5, "Nabisco", 8, "Chocolate", 220, True)

gondola_galletitas = Gondola(1, "galletitas", [sonrisas, pitusas_frutilla, oreos],)