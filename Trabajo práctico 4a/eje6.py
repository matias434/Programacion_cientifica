class cliente:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
    def depositar(self, monto):
        self.cantidad += monto
    def extraer(self, monto):
        if monto <= self.cantidad:
            self.cantidad -= monto
        else:
            print("Fondos insuficientes")
    def mostrar_total(self):
        return self.cantidad
class banco:
    def __init__(self):
        self.cliente1 = cliente("matias", 1000)
        self.cliente2 = cliente("luis", 1500)
        self.cliente3 = cliente("maria", 2000)
    def operar(self):
        self.cliente1.depositar(500)
        self.cliente2.extraer(200)
        self.cliente3.depositar(300)
    def deposito_total(self):
        total = (self.cliente1.mostrar_total() +
                 self.cliente2.mostrar_total() +
                 self.cliente3.mostrar_total())
        print(f"Depósito total en el banco: {total}")
b = banco()
b.operar()
b.deposito_total()
    
        

