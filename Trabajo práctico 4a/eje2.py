class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 6:
            print(f"{self.nombre} aprobó con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} no aprobó. Nota: {self.nota}.")
print("--- Alumno 1 ---")
alumno1 = Alumno("Lucía", 8)
alumno1.mostrar_datos()
alumno1.resultado()

print("\n--- Alumno 2 ---")
alumno2 = Alumno("Juan", 4)
alumno2.mostrar_datos()
alumno2.resultado()