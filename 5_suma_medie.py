numere = []
for i in range(3):
    numar = float(input("Introduceți un număr: "))
    numere.append(numar)

# Calculăm suma
suma = sum(numere)

# Calculăm media
media = suma / len(numere)

# Afișăm rezultatele
print("Suma celor trei numere este:", suma)
print("Media celor trei numere este:", media)