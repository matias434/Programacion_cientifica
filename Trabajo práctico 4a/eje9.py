class persona:
    def __init__(self,nombre="",edad=None, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        if isinstance(nombre,str):
            self.nombre = nombre
        else:
            raise ValueError("El nombre debe ser una cadena de texto")

    def get_edad(self):
        return self.edad

    def set_edad(self,edad):
        if isinstance(edad,int) and edad >= 0:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un número entero no negativo")

    def get_dni(self):
        return self.dni

    def set_dni(self,dni):
        if isinstance(dni,str) and dni.isdigit() and len(dni) == 8:
            self.dni = dni
        else:
            raise ValueError("El DNI debe ser una cadena de 8 dígitos")

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad is not None and self.edad >= 18

p = persona()
p.set_nombre("Matias")
p.set_edad(21)
p.set_dni("12345678")

p.mostrar()
print("¿Es mayor de edad?", p.esMayorDeEdad())