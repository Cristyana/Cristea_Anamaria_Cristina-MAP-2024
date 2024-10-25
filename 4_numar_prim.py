# Citim numărul de la tastatură

numar = int(input("Introduceți un număr: "))

if numar > 1:
    este_prim = True
    for i in range(2, int(numar / 2) + 1):
        if numar % i == 0:
            este_prim = False
            break
else:
    este_prim = False

if este_prim:
    print("Numărul este prim.")
else:
    print("Numărul nu este prim.")