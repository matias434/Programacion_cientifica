class calculadora:
    def __init__(self):
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("ingrese el segundo valor: "))
    def sumar(self):
        return self.valor1 + self.valor2
    def restar(self):
        return self.valor1 - self.valor2
    def multiplicar(self):
        return self.valor1 * self.valor2
    def dividir(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"
calc = calculadora()
print("Suma:", calc.sumar())
print("Resta:", calc.restar())
print("Multiplicación:", calc.multiplicar())
print("División:", calc.dividir())