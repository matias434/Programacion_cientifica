class universidad:
    def __init__(self,nombre):
        self.nombre = nombre
class carrera:
    def __init__(self,especialidad):
        self.especialidad = especialidad
class estudiante:
    def __init__(self,nombre,edad,universidad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.universidad = universidad
        self.carrera = carrera
    
    def mostrar_datos(self):
        print(f"especialidad: {self.carrera.especialidad}")
        print(f"edad: {self.edad}")
        print(f"nombre: {self.nombre}")
        print(f"universidad: {self.universidad.nombre}")
uni1 = universidad("Universidad Nacional")
carr = carrera("Ingenieria en Sistemas")
persona = estudiante("Matias",21,uni1,carr)
persona.mostrar_datos()