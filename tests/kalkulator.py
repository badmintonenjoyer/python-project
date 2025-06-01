def dodaj(a, b):
    return a + b

def dziel(a, b):
    if b == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero")
    return a / b
