numeros = [5, 11, 13, 8, 20, 15, 9, 21, 3]

contador = 0

for num in numeros:
    if num > 10 and num % 2 != 0:
        contador += 1

print(f"Cantidad de números impares mayores que 10: {contador}")