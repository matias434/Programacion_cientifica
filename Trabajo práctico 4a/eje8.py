class Cuenta:
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir_datos(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    def mostrar_info(self):
        print("Caja de Ahorro:")
        self.imprimir_datos()

class PlazoFijo(Cuenta):
    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    def importe_interes(self):
        return self.cantidad * self.interes / 100

    def mostrar_info(self):
        print("Plazo Fijo:")
        self.imprimir_datos()
        print(f"Plazo: {self.plazo} meses")
        print(f"Interés: {self.interes}%")
        print(f"Total de interés: {self.importe_interes()}")

caja = CajaAhorro("Ana", 15000)
caja.mostrar_info()

print()

plazo = PlazoFijo("Luis", 20000, 12, 5)
plazo.mostrar_info()