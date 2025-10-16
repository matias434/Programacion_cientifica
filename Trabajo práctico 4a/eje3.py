class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleaños(self):
        self.edad += 1
       
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")

persona1 = persona("Ana", 25)
persona1.mostrar_datos()
persona1.cumpleaños()
print("Después de cumplir años:")
persona1.mostrar_datos()