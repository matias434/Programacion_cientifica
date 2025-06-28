def es_dni_valido(dni):
    return 7 <= len(str(dni)) <= 8

while True:
    nombre_completo = input("Ingrese el nombre completo del socio: ").strip()
    if nombre_completo == "":
        break

    while True:
        dni_str = input("Ingrese el DNI del socio: ").strip()
        if dni_str.isdigit() and es_dni_valido(dni_str):
            dni = dni_str
            break
        else:
            print("DNI inválido. Debe tener 7 u 8 dígitos. Intenta otra vez.")

    nombres = nombre_completo.split()
    primer_nombre = nombres[0]
    apellido = nombres[-1]
    long_apellido = len(apellido)

    primeros_digitos = dni[:3]

    identificador = f"{primer_nombre}{long_apellido}{primeros_digitos}"

    print(f"Identificador: {identificador}")