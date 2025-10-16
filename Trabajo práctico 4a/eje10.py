class cuenta:
    def __init__(self, titular="", cantidad=0):
        self.titular = titular
        self.cantidad = float(cantidad)
    def get_titular (self):
        return self.titular
    def set_titular (self, titular):
        if isinstance(titular,str):
            self.titular = titular
        else:
            raise ValueError("el titular debe ser obligatorio y una cadena de texto")
    def get_cantidad (self):
        return self.cantidad
    def set_cantidad (self, cantidad):
        if isinstance(cantidad,(int,float)):
            self.cantidad = float(cantidad)
        else:
            raise ValueError("la cantidad debe ser un número")
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    def retirar(self, cantidad):
        self.cantidad -= cantidad
c = cuenta("Carlos", 100.5)
c.mostrar()
c.ingresar(50)
c.retirar(30)
c.mostrar()

    
