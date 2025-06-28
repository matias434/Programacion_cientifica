import operaciones

resultado_suma = operaciones.suma(10, 5)
print(f"Suma: {resultado_suma}")

resultado_division = operaciones.division(10, 0)
print(f"División: {resultado_division}")

resultado_suma_error = operaciones.suma(10, "a")
print(f"Suma con error: {resultado_suma_error}")