# Citim lista de la tastatură și o transformăm în numere întregi
elemente = input("Introduceți elementele separate prin spațiu: ")
lista = [int(x) for x in elemente.split()]

# sortarea prin Bubble Sort
n = len(lista)
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if lista[j] > lista[j + 1]:
            # Schimbăm elementele dacă sunt în ordine greșită
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print("Lista sortată este:", lista)