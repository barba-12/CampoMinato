from tkinter import *
from tkinter import StringVar
import random
import tkinter
from tkinter import messagebox

def sconfitta():
    global matrice
    for i in range(len(matrice)):
        for y in range(len(matrice[0])):
            if matrice[i][y]["etichetta"] == 9:
                matrice[i][y]["bottone"].config(text="💣")
    scegli_opzione()

def vittoria():
    global matrice
    for i in range(len(matrice)):
        for y in range(len(matrice[0])):
            if matrice[i][y]["etichetta"] == 9:
                matrice[i][y]["bottone"].config(text="🌸") 
            if matrice[i][y]["bottone"].cget("bg") == "#0f6a08" and matrice[i][y]["etichetta"] != 9:
                matrice[i][y]["bottone"].config(bg="#9a9892")     
            elif matrice[i][y]["bottone"].cget("bg") == "#6eaa5e" and matrice[i][y]["etichetta"] != 9:
                matrice[i][y]["bottone"].config(bg="#838078")   
    scegli_opzione()

def scegli_opzione():
    global window, matrice
    righe = len(matrice)

    btn_opzione1 = Button(window, text="gioca ancora", command=lambda:scelta_fatta(window, "gioca ancora"), width=10, height=1, background="#6eaa5e")
    btn_opzione1.grid(row=righe+1, column=righe-2, padx=5, pady=5, columnspan=2)
    btn_opzione2 = Button(window, text="esci", command=lambda:scelta_fatta(window, "esci"), width=10, height=1, background="#6eaa5e")
    btn_opzione2.grid(row=righe+1, column=0, padx=5, pady=5, columnspan=2)

def scelta_fatta(finestra, scelta):
    if scelta == "gioca ancora":
        window.destroy()
        main(10, 10, 8, 3, 10)
    elif scelta == "esci":
        window.destroy()

def bandierina(event):
    global cella_da_scoprire, matrice, numero_bandiere, bandiere, primo_click, fine
    x, y = event.widget.grid_info()['row'] - 1, event.widget.grid_info()['column']
    bandiere.grid_forget()
    lista_numeri, lun_column, testo_attuale = [0,1,2,3,4,5,6,7,8,9, ""], len(matrice), matrice[x][y]["bottone"].cget("text")
    
    if fine == 0:
        if testo_attuale == "" and numero_bandiere != 0 and matrice[x][y]["bottone"].cget("bg") != "#838078" and matrice[x][y]["bottone"].cget("bg") != "#9a9892" and primo_click == False:
            matrice[x][y]["bottone"].config(text="🚩")  
            numero_bandiere -= 1
        elif numero_bandiere != 0 and matrice[x][y]["bottone"].cget("text") not in lista_numeri:
            matrice[x][y]["bottone"].config(text="")
            numero_bandiere += 1
        elif numero_bandiere == 0 and matrice[x][y]["bottone"].cget("text") == "🚩":
            matrice[x][y]["bottone"].config(text="")
            numero_bandiere = 1
    
    bandiere = Label(window, text=f"🚩 {numero_bandiere}", font=("Helvetica", 24))
    bandiere.grid(row=0, column=lun_column-2, columnspan=2)

def conta_bombe():
    righe, colonne = len(matrice), len(matrice[0])

    for i in range(righe):
        for y in range(colonne):
            if matrice[i][y]["etichetta"] != 9:
                c = 0
                if i > 0 and y > 0 and matrice[i-1][y-1]["etichetta"] == 9:
                    c += 1
                if i > 0 and matrice[i-1][y]["etichetta"] == 9:
                    c += 1
                if i > 0 and y < colonne-1 and matrice[i-1][y+1]["etichetta"] == 9:
                    c += 1
                if y > 0 and matrice[i][y-1]["etichetta"] == 9:
                    c += 1
                if y < colonne-1 and matrice[i][y+1]["etichetta"] == 9:
                    c += 1
                if i < righe-1 and y > 0 and matrice[i+1][y-1]["etichetta"] == 9:
                    c += 1
                if i < righe-1 and matrice[i+1][y]["etichetta"] == 9:
                    c += 1
                if i < righe-1 and y < colonne-1 and matrice[i+1][y+1]["etichetta"] == 9:
                    c += 1
                matrice[i][y]["etichetta"] = c

def conta_bombe_vicine(x, y):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0 <= i < len(matrice) and 0 <= j < len(matrice[0]) and matrice[i][j]["etichetta"] == 9:
                count += 1
    return count

def resetta_bombe(r, c):
    for i in range(r):
        for j in range(c):
            if matrice[i][j]["etichetta"] == 9:
                matrice[i][j]["etichetta"] = 0

def posizione_bombe(num_bombe, r, c, x, y):
    global cella_da_scoprire, primo_click
    posizionate, cella_da_scoprire, celle_vicine, vietate = 0, r * c - num_bombe, [[x, y], [x-1, y-1], [x-1, y], [x-1, y+1], [x, y+1], [x, y-1], [x+1, y-1], [x+1, y], [x+1, y+1]], []

    for i, j in celle_vicine:
        if 0 <= i < r and 0 <= j < c:
            vietate.append((i, j))

    while num_bombe != posizionate:
        rig, col = random.randrange(r), random.randrange(c)
        if (rig, col) not in vietate and matrice[rig][col]["etichetta"] != 9:
            matrice[rig][col]["etichetta"] = 9
            posizionate += 1
    
    while conta_bombe_vicine(x, y) != 0:
        resetta_bombe(r, c)
        posizionate = 0
        while num_bombe != posizionate:
            rig, col = random.randrange(r), random.randrange(c)
            if (rig, col) not in vietate and matrice[rig][col]["etichetta"] != 9:
                matrice[rig][col]["etichetta"] = 9
                posizionate += 1

def scopri_cella(x, y):
    global matrice, cella_da_scoprire, numero_bandiere, fine

    if matrice[x][y]["colore"] == "#6eaa5e":
        if matrice[x][y]["etichetta"] != 0:
            matrice[x][y]["bottone"].config(text=matrice[x][y]["etichetta"], bg="#838078")
        else:
            matrice[x][y]["bottone"].config(bg="#838078")
    else:
        if matrice[x][y]["etichetta"] != 0:
            matrice[x][y]["bottone"].config(text=matrice[x][y]["etichetta"], bg="#9a9892")
        else:
            matrice[x][y]["bottone"].config(bg="#9a9892")
    matrice[x][y]["scoperta"] = True

    if matrice[x][y]["etichetta"] == 0:
        righe = len(matrice)
        colonne = len(matrice[0])
        if x > 0 and y > 0 and matrice[x-1][y-1]["scoperta"] == False:
            scopri_cella(x-1, y-1)
        if x > 0 and matrice[x-1][y]["scoperta"] == False:
            scopri_cella(x-1, y)
        if x > 0 and y < colonne-1 and matrice[x-1][y+1]["scoperta"] == False:
            scopri_cella(x-1, y+1)
        if y > 0 and matrice[x][y-1]["scoperta"] == False:
            scopri_cella(x, y-1)
        if y < colonne-1 and matrice[x][y+1]["scoperta"] == False:
            scopri_cella(x, y+1)
        if x < righe-1 and y < colonne-1 and matrice[x+1][y+1]["scoperta"] == False:
            scopri_cella(x+1, y+1)
        if x < righe-1 and matrice[x+1][y]["scoperta"] == False:
            scopri_cella(x+1, y)
        if x < righe-1 and y > 0 and matrice[x+1][y-1]["scoperta"] == False:
            scopri_cella(x+1, y-1)
            
    if matrice[x][y]["etichetta"] == 9:
        fine = 1
        tkinter.messagebox.showerror("hai perso", "sconfitta")
        sconfitta()
    else:
        cella_da_scoprire -= 1
        if cella_da_scoprire == 0:
            fine = 1
            tkinter.messagebox.showinfo("hai vinto", "vittoria")
            vittoria()
            
def scopri_cella_ricorsione(event):
    global matrice, primo_click, fine

    if fine == 0:
        x, y = event.widget.grid_info()['row']-1, event.widget.grid_info()['column']

        if primo_click == True:
            r, c = len(matrice), len(matrice)
            if r == 10:
                posizione_bombe(10, r, c, x, y)
            elif r == 18:
                posizione_bombe(40, r, c, x, y)
            else:
                posizione_bombe(99, r, c, x, y)
            primo_click = False
            conta_bombe()
        
        if matrice[x][y]["bottone"].cget("text") != "🚩":
            matrice[x][y]["bottone"].config(background="grey")
            scopri_cella(x, y)

def aggiorna_timer():
    global tempo_trascorso, fine
    if fine == 0:  
        tempo_trascorso += 1
        mins, secs = divmod(tempo_trascorso, 60)
        formato_timer = '{:02d}:{:02d}'.format(mins, secs)
        label_timer.config(text=formato_timer)
        window.after(1000, aggiorna_timer)

def cambia_livello(*args):
    window.destroy()
    livello = livello_var.get()
    if livello == "Facile":
        main(10, 10, 8, 3, 10)
    elif livello == "Medio":
        main(18, 18, 7, 3, 40)
    elif livello == "Difficile":
        main(24, 24, 5, 2, 99)

def crea_griglia(r, c, lun, alt, bombe):   
    global window, tempo_trascorso, label_timer, matrice, cella_da_scoprire, numero_bandiere, bandiere, livello_var, fine

    window = Tk()
    window.title("campo minato")
    window.configure(bg="#15400e")

    fine, tempo_trascorso, numero_bandiere, lista_colori_pari, lista_colori_dispari, opzioni_livello = 0, 0, bombe, ["#6eaa5e", "#0f6a08"], ["#0f6a08", "#6eaa5e"], ["Facile", "Medio", "Difficile"]

    label_timer = Label(window, font=("Helvetica", 24), text="00:00")
    label_timer.grid(row=0, column=c//2 - 1, columnspan=2, pady=10) 

    aggiorna_timer()

    livello_var = StringVar(window)
    livello_var.set("Scegli difficoltà") 

    menu_livello = OptionMenu(window, livello_var, *opzioni_livello)
    menu_livello.grid(row=0, column=0, padx=5, pady=10, columnspan=4)

    livello_var.trace("w", cambia_livello)

    for i in range(r):
        matrice.append([])
        for j in range(c):
            colore = lista_colori_pari[j % 2] if i % 2 == 0 else lista_colori_dispari[j % 2]
            btn = Button(window, width=lun, height=alt, background=colore)
            btn.grid(row=i+1, column=j)
            btn.bind("<Button-1>", scopri_cella_ricorsione)
            btn.bind("<Button-3>", bandierina)
            matrice[i].append({"bottone": btn, "etichetta": 0, "scoperta": False, "colore": colore})
            
    bandiere = Label(window, text=f"🚩 {bombe}", font=("Helvetica", 24))
    bandiere.grid(row=0, column=c-2, columnspan=2)

def main(r, c, h, l, b):
    global matrice, primo_click
    primo_click = True
    matrice.clear()
    crea_griglia(r, c, h, l, b)            

matrice = []
main(10, 10, 8, 3, 10)
window.mainloop()