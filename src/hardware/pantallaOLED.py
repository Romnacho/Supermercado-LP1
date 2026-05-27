class PantallaOLED:
    def __init__ (self):
        self.__mensaje_actual = ""

    def mostrarTotal(self, total):
        self.__mensaje_actual = f"Total: ${total}"
        print(self.__mensaje_actual)