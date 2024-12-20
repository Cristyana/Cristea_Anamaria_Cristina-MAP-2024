from tkinter import *
from tkinter import messagebox
import random

obiect = Tk()
obiect.geometry("650x150")
obiect.title("Piatra Hartie Foarfeca")
reguli = ("Regulie jocului sunt :\n"
     "Piatra vs Hartie -> Hartie\n"
     "Piatra vs Foarfeca -> Piatra\n"
     "Hartie vs Foarfeca -> Foarfeca"
     )

for col in range(4):
  obiect.columnconfigure(col, weight=1)

label_reguli = Label(obiect, text=reguli, justify="center",fg="#050238", font=('Calibri',14,'bold','italic'))
label_reguli.grid(row=0,columnspan=3)
buton_piatra = Button(obiect, text="Piatra", width=10, command=lambda:joc("Piatra"))
buton_piatra.grid(row=1,column=0, sticky="ew", padx=5, pady=5)
buton_hartie = Button(obiect, text="Hartie", width=10, command=lambda:joc("Hartie"))
buton_hartie.grid(row=1,column=1, sticky="ew", padx=5, pady=5)
buton_foarfeca = Button(obiect, text="Foarfeca", width=10, command=lambda:joc("Foarfeca"))
buton_foarfeca.grid(row=1,column=2, sticky="ew", padx=5, pady=5)
scor_om = 0
scor_pc = 0
label_om = Label(obiect, text=f"Scorul tau: {scor_om}")
label_om.grid(row=0,column=3)
label_pc = Label(obiect, text=f"Scor PC: {scor_pc}")
label_pc.grid(row=0, column=4)
def resetare():
  global scor_om,scor_pc
  scor_pc = 0
  scor_om = 0
  label_om.config(text=f"Scorul tau: {scor_om}")
  label_pc.config(text=f"Scorul PC: {scor_om}")
  messagebox.showinfo("Resetat", "JOCUL A FOST RESETAT")
 
def joc(alegerea_mea):
  global scor_om,scor_pc
  optiuni = ["Piatra","Hartie","Foarfeca"]
  alegere_pc = random.choice(optiuni)
  mesaj = f"Pc-ul a ales: {alegere_pc} \n\n"
  if(alegerea_mea==alegere_pc):
    mesaj+="EGALITATE"
  elif (alegerea_mea=="Piatra" and alegere_pc=="Foarfeca") or\
  (alegerea_mea=="Hartie" and alegere_pc=="Piatra") or\
  (alegerea_mea=="Foarfeca" and alegere_pc=="Hartie"):
    mesaj+="AI CASTIGAT"
    scor_om+=1
  else:
    mesaj+="AI PIERDUT"
    scor_pc+=1
  label_om.config(text=f"Scorul tau: {scor_om}")
  label_pc.config(text=f"Scorul PC: {scor_pc}")

  if scor_om == 3:
    messagebox.showinfo("WINNER", "AI CASTIGAT JOCUL")
    resetare()
  elif scor_pc == 3:
    messagebox.showinfo("LOSER", "AI PIERDUT JOCUL")
    resetare()
  else:
    messagebox.showinfo("Rezultat", mesaj)


mainloop()
