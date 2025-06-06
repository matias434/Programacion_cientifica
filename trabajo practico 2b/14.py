precio = float(input("Ingrese el valor del precio: "))

if precio > 200:
    monto_final = precio * 0.8  
else:
    monto_final = precio

print(f"El monto que debe pagar el cliente es: ${monto_final:.2f}")