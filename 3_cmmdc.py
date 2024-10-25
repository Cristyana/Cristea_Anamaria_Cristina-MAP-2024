# Citim numerele de la tastatură
x = int(input("Introduceți primul număr: "))
y = int(input("Introduceți al doilea număr: "))

while y != 0:
    x, y = y, x % y

print("Cel mai mare divizor comun este:", x)