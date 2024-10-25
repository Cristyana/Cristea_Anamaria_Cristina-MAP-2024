# Citim numărul de la tastatură
numar = int(input("Introduceți un număr între 1 și 7: "))

# Definim un dicționar care mapază numerele la zilele săptămânii
zile_saptamana = {
    1: "Luni",
    2: "Marți",
    3: "Miercuri",
    4: "Joi",
    5: "Vineri",
    6: "Sâmbătă",
    7: "Duminică"
}

# Verificăm dacă numărul este valid și afișăm ziua corespunzătoare
if numar in zile_saptamana:
    print("Ziua săptămânii este:", zile_saptamana[numar])
else:
    print("Introduceți un număr între 1 și 7.")
