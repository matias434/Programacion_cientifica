class triángulo:
     def __init__(self, lado1,lado2,lado3):
            self.lado1 = lado1
            self.lado2 = lado2
            self.lado3 = lado3
     def perímetro(self):
                return self.lado1 + self.lado2 + self.lado3
     def lado_mayor(self):
                return max(self.lado1, self.lado2, self.lado3)
     def tipo(self):
                if self.lado1 == self.lado2 == self.lado3:
                    return "Equilátero"
                elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                    return "Isósceles"
                else:
                    return "Escaleno"
triángulo1 = triángulo(3, 4, 5)
print("Perímetro del triángulo:", triángulo1.perímetro())
print("Lado mayor del triángulo:", triángulo1.lado_mayor())
print("Tipo de triángulo:", triángulo1.tipo())
