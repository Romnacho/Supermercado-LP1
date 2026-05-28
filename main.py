from src.productos.categorias.bebidas import Bebidas
from src.productos.categorias.carne import Carne
from src.productos.categorias.facturas import Factura
from src.productos.categorias.fiambre import Fiambre
from src.productos.categorias.galletita import Galletita
from src.productos.categorias.limpieza import Limpieza
from src.productos.categorias.panaderia import Panaderia
from src.productos.categorias.perfumeria import Perfumeria
from src.productos.categorias.verdura import Verdura

from src.hardware.sensor import Sensor
from src.hardware.tablet import Tablet
from src.gondola.gondola import Gondola

from src.almacen.inventario import Inventario
from src.almacen.almacen import Almacen
from src.carrito.carrito import Carrito
from src.cliente.cliente import Cliente
from src.pedidos.proveedor import Proveedor
from src.hardware.lectordecodigo import LectorDeCodigoDeBarras
from src.hardware.pantallaOLED import PantallaOLED
from src.promos.promos import Promocion
from src.menu.menu import menu_principal

# BEBIDAS
coca = Bebidas(nombre="Coca Cola", precio=800, stock=2, stockMax=20, codigoBarras=1001, umbralMinimo=5, marca="Coca Cola", unid_x_paquete=1, cm3=500, sabor="cola", porcentajeAlcohol=0)
heineken = Bebidas(nombre="Heineken", precio=600, stock=7, stockMax=30, codigoBarras=1002, umbralMinimo=5, marca="Heineken", unid_x_paquete=1, cm3=330, sabor="malta", porcentajeAlcohol=5)
jugo = Bebidas(nombre="Cepita Naranja", precio=400, stock=10, stockMax=15, codigoBarras=1003, umbralMinimo=3, marca="Cepita", unid_x_paquete=1, cm3=200, sabor="naranja", porcentajeAlcohol=0)

# CARNE
asado = Carne(nombre="Asado", precio=3000, stock=10, stockMax=15, codigoBarras=2001, umbralMinimo=2, marca="Carnes del Sur", tipo_corte="asado", categoria="vacuno")
pollo = Carne(nombre="Pechuga de Pollo", precio=1500, stock=8, stockMax=12, codigoBarras=2002, umbralMinimo=2, marca="Granja del Sol", tipo_corte="pechuga", categoria="aviar")
lomo = Carne(nombre="Lomo", precio=5000, stock=5, stockMax=10, codigoBarras=2003, umbralMinimo=2, marca="Carnes del Sur", tipo_corte="lomo", categoria="vacuno")

# FACTURAS
medialuna = Factura(nombre="Medialuna", precio=200, stock=30, stockMax=50, codigoBarras=3001, umbralMinimo=10, marca="La Espiga", unid_x_paquete=6, tipo="medialuna")
vigilante = Factura(nombre="Vigilante", precio=150, stock=20, stockMax=40, codigoBarras=3002, umbralMinimo=10, marca="La Espiga", unid_x_paquete=6, tipo="vigilante")
cañon = Factura(nombre="Cañon", precio=180, stock=25, stockMax=45, codigoBarras=3003, umbralMinimo=10, marca="La Espiga", unid_x_paquete=6, tipo="cañon")

# FIAMBRE
jamon = Fiambre(nombre="Jamon Cocido", precio=2000, stock=5, stockMax=10, codigoBarras=4001, umbralMinimo=2, marca="Paladini", tipo_fiambre="jamon cocido")
salame = Fiambre(nombre="Salame", precio=2500, stock=4, stockMax=8, codigoBarras=4002, umbralMinimo=2, marca="Cagnoli", tipo_fiambre="salame")
mortadela = Fiambre(nombre="Mortadela", precio=1800, stock=6, stockMax=10, codigoBarras=4003, umbralMinimo=2, marca="Paladini", tipo_fiambre="mortadela")

# GALLETITAS
oreo = Galletita(nombre="Oreo", precio=500, stock=20, stockMax=30, codigoBarras=5001, umbralMinimo=5, marca="Nabisco", unid_x_paquete=3, sabor="chocolate", pesoNeto=117, tieneTACC=True)
traviata = Galletita(nombre="Traviata", precio=400, stock=15, stockMax=25, codigoBarras=5002, umbralMinimo=5, marca="Bagley", unid_x_paquete=2, sabor="vainilla", pesoNeto=100, tieneTACC=True)
sin_tacc = Galletita(nombre="Galletita Sin TACC", precio=600, stock=10, stockMax=15, codigoBarras=5003, umbralMinimo=3, marca="Maná", unid_x_paquete=1, sabor="arroz", pesoNeto=80, tieneTACC=False)

# LIMPIEZA
lavandina = Limpieza(nombre="Lavandina", precio=300, stock=20, stockMax=30, codigoBarras=6001, umbralMinimo=5, marca="Ayudin", unid_x_paquete=1, tipoAplicacion="superficies", inflamable=False, toxico=True, pesoNeto=1000)
detergente = Limpieza(nombre="Detergente", precio=400, stock=15, stockMax=25, codigoBarras=6002, umbralMinimo=5, marca="Magistral", unid_x_paquete=1, tipoAplicacion="vajilla", inflamable=False, toxico=False, pesoNeto=500)
desodorante_piso = Limpieza(nombre="Desodorante de Piso", precio=350, stock=10, stockMax=20, codigoBarras=6003, umbralMinimo=3, marca="Pino", unid_x_paquete=1, tipoAplicacion="pisos", inflamable=False, toxico=False, pesoNeto=750)

# PANADERIA
lactal = Panaderia(nombre="Pan Lactal", precio=500, stock=15, stockMax=20, codigoBarras=7001, umbralMinimo=5, marca="Bimbo", tipo_pan="lactal")
integral = Panaderia(nombre="Pan Integral", precio=600, stock=10, stockMax=15, codigoBarras=7002, umbralMinimo=3, marca="Bimbo", tipo_pan="integral")
brioche = Panaderia(nombre="Pan Brioche", precio=700, stock=8, stockMax=12, codigoBarras=7003, umbralMinimo=3, marca="La Panaderia", tipo_pan="brioche")

# PERFUMERIA
shampoo = Perfumeria(nombre="Shampoo", precio=800, stock=10, stockMax=15, codigoBarras=8001, umbralMinimo=3, marca="Head & Shoulders", unid_x_paquete=1, cm3=400, fragancia="mentol", importado=False)
perfume = Perfumeria(nombre="Perfume 212", precio=5000, stock=5, stockMax=10, codigoBarras=8002, umbralMinimo=2, marca="Carolina Herrera", unid_x_paquete=1, cm3=100, fragancia="floral", importado=True)
crema = Perfumeria(nombre="Crema Nivea", precio=600, stock=12, stockMax=20, codigoBarras=8003, umbralMinimo=3, marca="Nivea", unid_x_paquete=1, cm3=200, fragancia="neutro", importado=False)

# VERDURA
tomate = Verdura(nombre="Tomate", precio=500, stock=20, stockMax=30, codigoBarras=9001, umbralMinimo=5, marca="La Huerta", tipo_verdura="tomate")
papa = Verdura(nombre="Papa", precio=300, stock=25, stockMax=35, codigoBarras=9002, umbralMinimo=5, marca="La Huerta", tipo_verdura="papa")
lechuga = Verdura(nombre="Lechuga", precio=400, stock=15, stockMax=25, codigoBarras=9003, umbralMinimo=5, marca="La Huerta", tipo_verdura="lechuga")

# HARDWARE POR GONDOLA
sensor_bebidas = Sensor(idSensor=1, estado=True)
tablet_bebidas = Tablet(idTablet=1)

sensor_carnes = Sensor(idSensor=2, estado=True)
tablet_carnes = Tablet(idTablet=2)

sensor_facturas = Sensor(idSensor=3, estado=True)
tablet_facturas = Tablet(idTablet=3)

sensor_fiambres = Sensor(idSensor=4, estado=True)
tablet_fiambres = Tablet(idTablet=4)

sensor_galletitas = Sensor(idSensor=5, estado=True)
tablet_galletitas = Tablet(idTablet=5)

sensor_limpieza = Sensor(idSensor=6, estado=True)
tablet_limpieza = Tablet(idTablet=6)

sensor_panaderia = Sensor(idSensor=7, estado=True)
tablet_panaderia = Tablet(idTablet=7)

sensor_perfumeria = Sensor(idSensor=8, estado=True)
tablet_perfumeria = Tablet(idTablet=8)

sensor_verduras = Sensor(idSensor=9, estado=True)
tablet_verduras = Tablet(idTablet=9)

# GONDOLAS
gondola_bebidas = Gondola(idGondola=1, tipo="Bebidas", productos=[coca, heineken, jugo], sensores=[sensor_bebidas], tablet=tablet_bebidas, promo=3) #promo segunda unidad con descuento
gondola_carnes = Gondola(idGondola=2, tipo="Carnes", productos=[asado, pollo, lomo], sensores=[sensor_carnes], tablet=tablet_carnes, promo=0)
gondola_facturas = Gondola(idGondola=3, tipo="Facturas", productos=[medialuna, vigilante, cañon], sensores=[sensor_facturas], tablet=tablet_facturas, promo=0)
gondola_fiambres = Gondola(idGondola=4, tipo="Fiambres", productos=[jamon, salame, mortadela], sensores=[sensor_fiambres], tablet=tablet_fiambres, promo=0)
gondola_galletitas = Gondola(idGondola=5, tipo="Galletitas", productos=[oreo, traviata, sin_tacc], sensores=[sensor_galletitas], tablet=tablet_galletitas, promo=1)  #promo 2x1
gondola_limpieza = Gondola(idGondola=6, tipo="Limpieza", productos=[lavandina, detergente, desodorante_piso], sensores=[sensor_limpieza], tablet=tablet_limpieza, promo=0)
gondola_panaderia = Gondola(idGondola=7, tipo="Panaderia", productos=[lactal, integral, brioche], sensores=[sensor_panaderia], tablet=tablet_panaderia, promo=2)  #promo porcentaje
gondola_verduras = Gondola(idGondola=8, tipo="Verduras", productos=[tomate, papa, lechuga], sensores=[sensor_verduras], tablet=tablet_verduras, promo=0)
gondola_perfumeria = Gondola(idGondola=9, tipo="Perfumeria", productos=[shampoo, perfume, crema], sensores=[sensor_perfumeria], tablet=tablet_perfumeria, promo=0)

# PROMOS
promo_2x1 = Promocion(tipo=1, cantidad_necesaria=2, productos_descontados=1, porcentaje_descuento=0)
promo_descuento = Promocion(tipo=2, cantidad_necesaria=1, productos_descontados=0, porcentaje_descuento=20)
promo_segunda_unidad = Promocion(tipo=3, cantidad_necesaria=2, productos_descontados=1, porcentaje_descuento=50)

# INVENTARIO
inventario = Inventario(capacidadMaxDeposito=1000, umbralMinimoGlobal=10, cantPedido=30)

# ALMACEN
listaGondolas = [gondola_bebidas, gondola_carnes, gondola_facturas, gondola_fiambres,
                 gondola_galletitas, gondola_limpieza, gondola_panaderia, gondola_verduras, gondola_perfumeria]

almacen = Almacen(listaGondolas=listaGondolas, inventario=inventario, promos=[promo_2x1, promo_descuento, promo_segunda_unidad])

# registramos todos los productos en el almacen
productos = [coca, heineken, jugo, asado, pollo, lomo, medialuna, vigilante, cañon,
             jamon, salame, mortadela, oreo, traviata, sin_tacc, lavandina, detergente,
             desodorante_piso, lactal, integral, brioche, shampoo, perfume, crema,
             tomate, papa, lechuga]

for producto in productos:
    almacen.registrarProducto(producto)
    inventario.getDeposito().agregarStock(producto.getCodigoBarras(), 10)  #stock inicial en deposito x producto

# CARRITO
lector = LectorDeCodigoDeBarras(idLector=1)
pantalla = PantallaOLED()
carrito = Carrito(lectorBarra=lector, pantalla=pantalla)

# CLIENTE
cliente = Cliente(idCliente=1, nombre="Carlitos", carrito=carrito)

# PROVEEDOR
proveedor = Proveedor(nombreEmpresa="Proveedor 1", cuit=123456789, mail="pedidos@gmail.com", marcasQueProvee=["Todas"])

menu_principal(almacen, carrito, cliente, proveedor, inventario, lector)