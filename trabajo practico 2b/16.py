X = int(input("Ingrese el número límite X: "))

a, b = 0, 1

while a <= X:
    print(a, end=' ')
    a, b = b, a + b