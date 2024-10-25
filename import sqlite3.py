import sqlite3
import random
def adauga_informatii():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS scuze (id INTEGER PRIMARY KEY AUTOINCREMENT, scuze_text TEXT NOT NULL)")
    scuza_noua = input("Introdu o noua scuza: ")
    cursor.execute('INSERT INTO scuze (scuze_text) VALUES (?)', (scuza_noua,))
    conn.commit()
    print("Scuza a fost adaugata in BD ")
    conn.close()
 
def generare_scuza():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT scuze_text FROM scuze')
    scuze = cursor.fetchall()
    scuza2 = random.choice(scuze)[0]
    print("Scuza ta este: ",scuza2)
 
def stergere_scuza():
    conn = sqlite3.connect('scuze.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM scuze')
    scuze = cursor.fetchall()
    for scuza in scuze:
        print(f"{scuza[0]}: {scuza[1]}")
   
    id_scuza_stergere = input("Introdu id-ul scuzei pe care vrei sa o stergi")
    cursor.execute('DELETE FROM scuze WHERE id = ?', (id_scuza_stergere,))
    conn.commit()
    print("Scuza a fost stearsa cu succes !")
    conn.close()    
   
# generare_scuza()
stergere_scuza()
#adauga_informatii()