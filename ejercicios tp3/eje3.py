def dni_valido(dni):
    str_dni = str(dni)
    return 7 <= len(str_dni) <= 8

dni = input("Ingresa tu número de dni: ")
if dni_valido(dni):
    print("El dni es válido.")
else:
    print("El dni no es válido.")