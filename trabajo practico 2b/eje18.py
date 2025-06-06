try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero. Verifica la operación.")

lista = [1, 2, 3, 4, 5]
try:
    elemento = lista[10]
except IndexError:
    print("Error: Índice fuera de rango en la lista. Verifica la longitud de la lista.")

colores = { 'rojo':'red', 'verde':'green', 'negro':'black' }
try:
    print(colores['blanco'])
except KeyError:
    print("Error: La clave 'blanco' no existe en el diccionario. Verifica las claves disponibles.")

try:
    resultado = 15 + "20"
except TypeError:
    print("Error: No se puede sumar un entero con una cadena. Convierte la cadena a número si es necesario.")