# Citim cele trei unghiuri de la tastatură
unghi1 = float(input("Introduceți unghiul 1: "))
unghi2 = float(input("Introduceți unghiul 2: "))
unghi3 = float(input("Introduceți unghiul 3: "))

suma_unghiuri = unghi1 + unghi2 + unghi3

# Verificăm dacă unghiurile pot forma un triunghi
if suma_unghiuri == 180 and unghi1 > 0 and unghi2 > 0 and unghi3 > 0:
    print("Unghiurile pot forma un triunghi.")
else:
    print("Unghiurile nu pot forma un triunghi.")