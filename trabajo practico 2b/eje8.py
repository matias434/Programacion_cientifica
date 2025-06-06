import math

a = float(input("Ingresa a: "))
b = float(input("Ingresa b: "))
c = float(input("Ingresa c: "))

lado_mayor = max(a, b, c)

if lado_mayor == a:
    cateto1, cateto2 = b, c
elif lado_mayor == b:
    cateto1, cateto2 = a, c
else:
    cateto1, cateto2 = a, b

comparacion = math.isclose(lado_mayor ** 2, cateto1 ** 2 + cateto2 ** 2)

if comparacion:
    
    area = (cateto1 * cateto2) / 2
    
    perimetro = a + b + c
    print(f"El área del triángulo es {area}")
    print(f"El perímetro del triángulo es {perimetro}")
else:
    print("Los lados no forman un triángulo rectángulo válido.")