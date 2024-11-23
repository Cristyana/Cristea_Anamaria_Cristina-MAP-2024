import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
import os
import pandas as pd

elevi = []  # Listă globală pentru a stoca datele elevilor

# Obține directorul curent al fișierului cu codul sursă
current_directory = os.path.dirname(os.path.abspath(__file__))
qr_folder = os.path.join(current_directory, "Coduri_QR")

# Creează folderul "Coduri QR" dacă nu există
if not os.path.exists(qr_folder):
    os.makedirs(qr_folder)

# Funcție pentru a genera cod QR
def generate_qr(data, filename):
    try:
        filepath = os.path.join(qr_folder, filename)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filepath)
    except Exception as e:
        print(f"Error generating QR code: {e}")

# Funcție pentru a salva un elev și a genera codul QR
def add_student():
    nume = entry_nume.get().strip()
    clasa = entry_clasa.get().strip()

    # Validare input
    if not all(char.isalpha() or char.isspace() or char == '-' for char in nume):
        messagebox.showerror("Eroare", "Numele trebuie să conțină doar litere și spații!")
        return
    if not clasa:
        messagebox.showerror("Eroare", "Clasa nu poate fi goală!")
        return
    
    elev = {
        "Nume": nume,
        "Clasa": clasa,
            }
    elevi.append(elev)

    # Mesaj de întâmpinare
    messagebox.showinfo("Salut", f"Hello, {nume}. Îți vom genera codul QR.")

    # Crearea textului pentru codul QR
    qr_data = f"Nume: {nume}\nClasa: {clasa}\nLiceul Teoretic"
    filename = f"Clasa_{clasa.replace(' ', '_')}_{nume.replace(' ', '_')}.png"
    # Generare cod QR
    generate_qr(qr_data, filename)

    # Confirmare și deschidere folder
    messagebox.showinfo(
        "Succes",
        f"Codul QR pentru {nume} a fost generat!\n"
        f"Fișier: {filename} salvat în {qr_folder}"
    )
    #os.startfile(qr_folder)

    # Golește câmpurile de input
    entry_nume.delete(0, tk.END)
    entry_clasa.delete(0, tk.END)

def show_students():
    if not elevi:
        messagebox.showinfo("Informație", "Nu există elevi înregistrați.")
        return

    # Creează o fereastră nouă
    list_window = tk.Toplevel(root)
    list_window.title("Lista Elevilor")
    list_window.geometry("600x300")

    # Textarea pentru afișarea datelor
    text_area = tk.Text(list_window, wrap=tk.WORD)
    text_area.pack(fill=tk.BOTH, expand=True)

    # Adaugă elevii în text_area
    for elev in elevi:
       text_area.insert(tk.END, f"Nume: {elev['Nume']}, Clasa: {elev['Clasa']}\n")
       text_area.insert(tk.END, "-" * 40 + "\n")

def export_to_excel():
    if not elevi:
        messagebox.showinfo("Informație", "Nu există elevi înregistrați pentru export!")
        return

    # Creare DataFrame din lista de elevi
    try:
        df = pd.DataFrame(elevi)
        
        # Selectează locația fișierului pentru salvare
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Fișiere Excel", "*.xlsx"), ("Toate fișierele", "*.*")],
            title="Salvează fișierul Excel"
        )
        if not file_path:  # Dacă utilizatorul anulează dialogul
            return

        # Salvare în Excel
        df.to_excel(file_path, index=False)

        # Confirmare
        messagebox.showinfo("Succes", f"Lista elevilor a fost exportată cu succes în:\n{file_path}")
    except Exception as e:
        messagebox.showerror("Eroare", f"A apărut o problemă la exportul în Excel: {e}")


# Funcție pentru a citi baza de date din Excel
def read_db():
    file_path = filedialog.askopenfilename(
        title="Selectează fișierul Excel",
        filetypes=(("Fișiere Excel", "*.xlsx *.xls"), ("Toate fișierele", "*.*"))
    )
    if not file_path:
        return  # Dacă utilizatorul închide dialogul fără a selecta un fișier
    
    try:
        # Citire fișier Excel
        data = pd.read_excel(file_path)
        
        # Verificare dacă există coloanele necesare
        if "Nume" not in data.columns or "Clasa" not in data.columns:
            messagebox.showerror("Eroare", "Verificati ca fisierul Excel sa contina coloanele necesare!")
            return
        
        # Iterare peste rânduri și generare coduri QR
        for _, row in data.iterrows():
            nume = str(row['Nume']).strip()
            clasa = str(row['Clasa']).strip()

            # Validare date
            if not all(char.isalpha() or char.isspace() or char == '-' for char in nume):
                print(f"Sarim peste intrarea invalida: {nume}")
                continue
            if not clasa:
                print(f"Sarim peste intrarea invalida: {clasa}")
                continue
            
            qr_data = f"{nume}\n{clasa}\nLiceul Teoretic"
            filename = f"{clasa.replace(' ', '_')}_{nume.replace(' ', '_')}.png"
            generate_qr(qr_data, filename)
        
        # Confirmare finală și deschidere folder
        messagebox.showinfo(
            "Succes", f"Codurile QR au fost generate pentru toți elevii din fișier!\nFișiere salvate în {qr_folder}"
        )
        os.startfile(qr_folder)

    except Exception as e:
        messagebox.showerror("Eroare", f"A apărut o problemă la citirea fișierului: {e}")

# Creare fereastră principală
root = tk.Tk()
root.title("Generator coduri QR pentru elevi")
root.geometry("")

# Frame-uri pentru partea stângă și dreaptă
left_frame = tk.Frame(root, width=300, height=250)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(root, width=300, height=250)
right_frame.pack(side="right", fill="both", expand=True)

# Componente Stânga (Introducere Manuală)
label_manual = tk.Label(left_frame, text="Generează codurile manual", font=("Arial", 12, "bold"))
label_manual.pack(pady=10)

label_nume = tk.Label(left_frame, text="Numele complet al elevului:")
label_nume.pack(pady=5)
entry_nume = tk.Entry(left_frame, width=30)
entry_nume.pack(pady=5)

label_clasa = tk.Label(left_frame, text="Clasa:")
label_clasa.pack(pady=5)
entry_clasa = tk.Entry(left_frame, width=20)
entry_clasa.pack(pady=5)

submit_button = tk.Button(left_frame, text="Adaugă Elev și Generează QR", command=add_student)
submit_button.pack(pady=20)

# Frame suplimentar pentru a alinia butoanele pe același rând
button_frame = tk.Frame(left_frame)
button_frame.pack(pady=10)

show_button = tk.Button(button_frame, text="Afișează Lista Elevilor", command=show_students)
show_button.pack(side=tk.LEFT, padx=5)

export_button = tk.Button(button_frame, text="Exportă Lista în Excel", command=export_to_excel)
export_button.pack(side=tk.LEFT, padx=5)

# Componente Dreapta (Citire Excel) 
label_excel_title = tk.Label(right_frame, text="Generează codurile automat", font=("Arial", 12, "bold"))
label_excel_title.pack(pady=10)

label_excel_info = tk.Label(
    right_frame,
    text="Selectează fișierul .xls / .xlsx și generează automat codurile elevilor folosind butonul de mai jos.\nAtentie: fișierul trebuie să conțină coloanele 'Numele și prenumele elevului' și 'Clasa'!",
    font=("Arial", 10),
    justify="center",
    wraplength=250
)
label_excel_info.pack(pady=10)

read_button = tk.Button(right_frame, text="Încarcă fișierul & Generează QR", command=read_db)
read_button.pack(pady=20)


root.mainloop()
