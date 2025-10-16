class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
    def es_mayor_de_edad(self):
        return self.edad >= 18

    def mensaje_mayor_edad(self):
        if self.es_mayor_de_edad():
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")
print("--- Persona 1 (Mayor de edad) ---")
persona1 = Persona("Carlos", 30)
persona1.mostrar_datos()
persona1.mensaje_mayor_edad()

print("\n--- Persona 2 (Menor de edad) ---")
persona2 = Persona("matias", 15)

persona2.mostrar_datos()
persona2.mensaje_mayor_edad()