from tkinter import *

# Crearea ferestrei principale
obiect = Tk()
obiect.title("Tipuri de persoane")
obiect.geometry("")

# Variabilele StringVar
variabila_gen = StringVar(value="masculin")
variabila_tip = StringVar(value="fumator")

# Frame pentru alegerea tipului
frame_tip_on = LabelFrame(obiect, text="Alegere")
frame_tip_on.pack(side="left", padx=10, pady=10)  # Adăugăm un padding pentru un aspect mai plăcut

# Radiobutton-uri pentru tipul de persoană
Radiobutton(frame_tip_on, text="Fumator", variable=variabila_tip, value="fumator").pack(anchor="w")
Radiobutton(frame_tip_on, text="Nefumator", variable=variabila_tip, value="nefumator").pack(anchor="w")

# Frame pentru alegerea genului
frame_gen = LabelFrame(obiect, text="Gen")
frame_gen.pack(side="left", padx=10, pady=10)  # Adăugăm un padding pentru un aspect mai plăcut

# Radiobutton-uri pentru gen
Radiobutton(frame_gen, text="Masculin", variable=variabila_gen, value="masculin").pack(anchor="w")
Radiobutton(frame_gen, text="Feminin", variable=variabila_gen, value="feminin").pack(anchor="w")

# Etichetă pentru afișarea rezultatului
label_rezultat = Label(obiect, text="")
label_rezultat.pack(side="bottom", pady=10)

# Buton pentru a afla rezultatul
buton_actiune = Button(obiect, text="Afla raspunsul", command=lambda: afla())
buton_actiune.pack()

# Funcția care află răspunsul
def afla():
    if variabila_gen.get() == "masculin":
        gen = "barbat"
        fumator = "fumator" if variabila_tip.get() == "fumator" else "nefumator"
    else:
        gen = "femeie"
        fumator = "fumatoare" if variabila_tip.get() == "fumator" else "nefumatoare"
    
    mesaj = f"Esti {gen} {fumator}"
    label_rezultat.config(text=mesaj)

# Bucla principală
mainloop()
