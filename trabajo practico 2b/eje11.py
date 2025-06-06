valores = [12, 7, 25, 3, 18, 30, 5]

maximo = valores[0]
minimo = valores[0]

for num in valores:
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num

print(f"Valor máximo: {maximo}")
print(f"Valor mínimo: {minimo}")