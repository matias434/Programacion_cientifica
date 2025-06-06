puntos = int(input("Ingrese la cantidad de puntos acumulados: "))

if puntos > 10000:
    print("Genial, lo has hecho fenomenal.")
elif 6000 <= puntos <= 9999:
    print("Excelente, eres muy dedicado.")
elif 3000 <= puntos <= 5999:
    print("Muy bien, sigue así de constante.")
elif 1000 <= puntos <= 2999:
    print("Bien, sigue aprendiendo.")
else:
    print("Es un buen comienzo, no pares.")