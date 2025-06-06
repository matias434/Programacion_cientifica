numeros = [11, 21, 31, 45, 18, 9, 30, 22]

contador = 0

for num in numeros:
    if num > 15 and num % 3 == 0:
        contador += 1
        
print(f"Cantidad de números múltiplos de 3 y mayores que 15: {contador}")