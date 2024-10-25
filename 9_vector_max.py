# Citim lista de la tastatură și o transformăm în numere întregi
elemente = input("Introduceți elementele vectorului separate prin spațiu: ")
vector = [int(x) for x in elemente.split()]

maxim = vector[0]

# Parcurgem vectorul pentru a găsi valoarea maximă
for elem in vector:
    if elem > maxim:
        maxim = elem

print("Valoarea maximă din vector este:", maxim)