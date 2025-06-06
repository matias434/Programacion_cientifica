precio_por_kilo = float(input("Ingrese el precio por kilo de manzana: "))

kilos = float(input("Ingrese la cantidad de kilos comprados: "))

if kilos <= 2:
    descuento = 0
elif kilos <= 5:
    descuento = 0.10
elif kilos <= 10:
    descuento = 0.15
else:
    descuento = 0.20

precio_total = precio_por_kilo * kilos

valor_descuento = precio_total * descuento

precio_final = precio_total - valor_descuento

print(f"El total a pagar por {kilos} kilos es: ${precio_final:.2f}")