import cmath  # cmath gestionează și rădăcinile complexe

# introducerea  valorilor de la tastatură
a = float(input("Introduceți valoarea lui a: "))
b = float(input("Introduceți valoarea lui b: "))
c = float(input("Introduceți valoarea lui c: "))


delta = b**2 - 4 * a * c


if delta > 0:
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print("Ecuația are două soluții reale distincte:", x1.real, "și", x2.real)

elif delta == 0:
    x = -b / (2 * a)
    print("Ecuația are o soluție reală dublă:", x)

else:
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)
    print("Ecuația are două soluții complexe:", x1, "și", x2)