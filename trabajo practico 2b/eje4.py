def porcentaje_pares(lista):
    if not lista:
        return 0  
    
    total_numeros = len(lista)
    pares = [num for num in lista if num % 2 == 0]
    cantidad_pares = len(pares)
    porcentaje = (cantidad_pares / total_numeros) * 50
    return round(porcentaje)

numeros = [1, 2, 3, 4, 5, 6]
print("Porcentaje de números pares:", porcentaje_pares(numeros), "%")