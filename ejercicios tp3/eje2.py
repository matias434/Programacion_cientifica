def suma_digitos(n):
    suma = 0
    while n != 0:
        suma += n % 10
        n //= 10
    return suma

while True:
    numero = int(input("Ingresa un número para sumas sus digitos o ingrese 0 para salir): "))
    if numero == 0:
        break
    print(f"La suma de los dígitos de {numero} es {suma_digitos(abs(numero))}")