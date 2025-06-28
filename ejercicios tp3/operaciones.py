def suma(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError
        return a + b
    except TypeError:
        print("error: tipo de dato no válido.")
        return None

def resta(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError
        return a - b
    except TypeError:
        print("error: tipo de dato no válido.")
        return None

def producto(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError
        return a * b
    except TypeError:
        print("error: tipo de dato no válido.")
        return None

def division(a, b):
    try:
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except TypeError:
        print("error: tipo de dato no válido.")
        return None
    except ZeroDivisionError:
        print("error: no es posible dividir entre cero.")
        return None