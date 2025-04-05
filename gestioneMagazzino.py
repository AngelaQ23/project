from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
from tkinter import filedialog
import customtkinter as ctk
from math import *
import re
import os



#Implementazione dell'interfaccia grafica della finestra principale
root = ctk.CTk() 

root.title("Gestione magazzino") 
root.geometry('800x600+350+50')
root.iconbitmap('./boxes.ico')
root.minsize(400,400)
root.maxsize(800,500)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")
root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)
root.rowconfigure(4, weight = 1)
root.rowconfigure(5, weight = 1)
root.rowconfigure(6, weight = 1)
root.rowconfigure(7, weight = 1)
root.rowconfigure(8, weight = 1)
root.rowconfigure(9, weight = 1)
root.rowconfigure(10, weight = 1)

#creo una menubar
menubar = Menu(root)
root.config(menu= menubar)
file_menu = Menu(menubar,tearoff=0)
menubar.add_cascade(label = 'File', menu = file_menu)



#creo delle finestre tab da poter sfogliare per le varie sezioni
finestre_tab = ttk.Notebook(root) 
finestre_tab.grid(columnspan=2,rowspan=2,ipadx=500,ipady=500)
frame1 = Frame(finestre_tab,width = 400, height=400) #frame per la tab calcolo
frame2 = Frame(finestre_tab,width = 400, height= 400)#frame per la tab della tabella di registro
frame3 = Frame(finestre_tab,width = 400, height= 400)#frame per la tab scorte


finestre_tab.add(frame1,text = "  Calcolo EOQ ",padding=1) 
finestre_tab.add(frame2,text = "  Tabella ordini registrati  ",padding=1)#creo una tab per calcolo
finestre_tab.add(frame3,text = "  Scorte   ",padding=1)#creo una tab per scorte

#creo un'etichetta di indicazioni 
etichetta = Label(frame1, text = "Inserisci i valori da analizzare per il calcolo dell' EOQ : ",font='Times')
etichetta.grid(column = 0, row = 0,padx = 4,ipady = 20,sticky = 'w')


#Domanda annua
valore_d = IntVar
d_label = Label(frame1, text = "Domanda annua",font='Times')
d_entry= ttk.Entry(frame1, textvariable = valore_d,justify=RIGHT)
d_entry.focus()
unita_label = Label(frame1,text = 'unità',font='Times') #creo un'etichetta per descrivere contenuto entry
d_label.grid(column = 0, row = 2,padx = 5, sticky = 'w')
d_entry.grid(column = 0, row = 3, padx = 5, ipadx =1,sticky = 'w')
unita_label.grid(column = 0, row = 3, padx = 145,sticky='w')


#Creo una entry per inserire il codice del prodotto
valore_id = StringVar
id_label = Label(frame1, text = "Codice prodotto",font='Times')
id_entry= ttk.Entry(frame1, textvariable = valore_id)
id_label.grid(column = 1, row = 2, sticky='w')
id_entry.grid(column=1,row=3)

#Costo di setup per ordine mensile
valore_s = IntVar
s_label = Label(frame1, text = 'Costo di setup per ordine mensile',font='Times')
s_entry = ttk.Entry(frame1, textvariable = valore_s,justify=RIGHT)
valuta_label1 = Label(frame1,text = '€')
valuta_label1.grid(column = 0, row = 5, padx = 130,sticky= 'w')
s_entry.grid(column = 0, row = 5,padx = 5,sticky = 'w' )
s_label.grid(column = 0, row = 4,padx = 5,sticky = 'w'  )

#Costo di mantenimento delle scorte per unità per anno
valore_h = IntVar
h_label = Label(frame1, text = 'Costo di mantenimento delle scorte',font='Times')
h_entry = ttk.Entry(frame1, textvariable = valore_h,justify=RIGHT)
valuta_label2 = Label(frame1,text = '€')
valuta_label2.grid(column = 0, row = 7, padx = 130,sticky= 'w')
h_entry.grid(column = 0, row = 7,padx = 5,sticky = 'w' )
h_label.grid(column = 0, row = 6,padx = 5,sticky = 'w' )



#Definizione della funzione per calcolare EOQ
def quantita_riordino():
    d = d_entry.get()  
    s = s_entry.get().replace(",",".")        #uso replace per cambiare il separatore dato che comunemente 
    h = h_entry.get().replace(",",".")        #usiamo la virgola invece del punto
    
    try:
        lotto_econom_ord = round(sqrt(2*int(d)*float(s)/float(h)))

    #finestra di errore per tentativo di dividere per zero        
    except ZeroDivisionError: 
        messagebox.showerror(title = "Errore", message = "Attenzione, tentativo di divisione per zero")

    #finestra di errore per altri valori non consoni inseriti    
    except ValueError: 
        messagebox.showerror(title = "Errore", message = "Attenzione, i valori inseriti non sono validi")
    
    #se non ci sono errori restituisco il valore dell'EOQ    
    else:
         global risultato
         risultato = Label(frame1, text= "Risultato : " + (str((lotto_econom_ord)).replace(".",",") + " unità"),
                           font='Times')
         risultato.grid(column = 0, row = 8, sticky = 'w' )

         #disattivo il bottone calcola in modo da obbligare l'azzeramento prima di un nuovo calcolo
         calcola.configure(state = DISABLED)

         #chiedo all'utente se vuole registrare i dati
         risposta= messagebox.askyesno(title = "Registra dati", message = "Vuoi salvare i dati nella tabella ? ")
         if risposta:
             tabella.insert('',END,values = (f'{id_entry.get()}',f'{d} unità',f'{s} €', f' {h}€',
                                             f'{lotto_econom_ord} unità'))
        
         

         #EOQ totalmente da rifare 
         #quantità ottimali e spese totali da aggiungere
        
         #analizzare i dati di 3 anni di esercizio

         


#Bottone per calcolo EOQ
calcola = ctk.CTkButton(frame1, text = 'Calcola', command = quantita_riordino,width=20,fg_color='grey20')
calcola.grid(column = 0, row = 9 ,padx = 5,pady= 5,sticky = 'wns' )


#Funzione che azzera tutti i campi per poter fare un nuovo calcolo
def azzera():
    d_entry.delete(0, END)
    s_entry.delete(0, END)
    h_entry.delete(0, END)
    id_entry.delete(0,END)
    d_entry.focus()
    risultato.destroy()
   
    #riattivo il bottone calcola
    calcola.configure(state = NORMAL)

    
#Bottone della funzione azzera
azzera = ctk.CTkButton(frame1, text = "Azzera", command = azzera,width=20)
azzera.grid(column = 0, row = 9,padx = 65,pady=5,sticky = 'w' )

#tabella per tenere conto dei valori ottenuti e poterli analizzare
colonne = ('codice prodotto','domanda','costo setup','costo di mantenimento','EOQ')#agg spesev tot
tabella = ttk.Treeview(frame2,columns = colonne, show = 'headings',height=20,selectmode='browse')
tabella.heading('codice prodotto', text = 'Codice prodotto')
tabella.heading('domanda', text = 'Domanda annua')
tabella.heading('costo setup', text = 'Costo setup')
tabella.heading('costo di mantenimento', text = 'Costo mantenimento merce ')
tabella.heading('EOQ', text = 'EOQ calcolato')
# tabella.heading('spese totali', text = 'Spese totali ordine effettuato')


#Definisco larghezza colonne
tabella.column('codice prodotto', width=95)
tabella.column('domanda', width=100)
tabella.column('costo setup', width=85)
tabella.column('costo di mantenimento', width=160)
tabella.column('EOQ', width=100)
# tabella.column('spese totali', width=170)


tabella.grid(row = 0,column = 0,sticky='nsew')
barra_scorrimento = ttk.Scrollbar(frame2,orient = 'vertical',command = tabella.yview)
barra_scorrimento.grid(row = 0,column = 1, sticky = 'ns')

#Creo una sezione che tiene conto delle scorte
frame_scorte1= Frame(frame3, width= 300,height= 600, background='grey22')
frame_scorte2= Frame(frame3, width= 400,height= 600,background='grey20')
frame_scorte1.grid(column = 0, row = 0)
frame_scorte2.grid(column = 1, row = 0)

colonne = ('codice prodotto','unità in magazzino','punto di riordino')
tabella_scorte = ttk.Treeview(frame_scorte2,columns = colonne, show = 'headings',height=28,selectmode= 'extended')
tabella_scorte.heading('codice prodotto', text = 'Codice prodotto')
tabella_scorte.heading('unità in magazzino', text = 'Unità in magazzino')
tabella_scorte.heading('punto di riordino', text = 'Punto di riordino')

tabella_scorte.column('codice prodotto', width=95)
tabella_scorte.column('unità in magazzino', width=100)
tabella_scorte.column('punto di riordino', width=85)

tabella_scorte.grid(column = 1,row = 0)
#Creo una funzione per salvare il file della tabella 
def salva_dati():

    filename = filedialog.asksaveasfile(mode = 'w',title = 'Salva file' ,defaultextension='*.txt')
    
    for line in tabella.get_children():
        

        filename.write(str(tabella.item(line)['values']))
        
        
#aggiungo la funzione alla menubar            
file_menu.add_command(label = 'Salva', command = salva_dati)

#Creo una funzione per aprire un file già creato
def apri_file():
    tipi_file = (('file di testo', '*.txt'),('tutti i file',' *.*'))
    filename = filedialog.askopenfilename(title = 'Apri un file', initialdir= '/',filetypes=tipi_file)

    f= open(filename,'r')

    for line in f:
        lista = re.split(',',line)
        
            
        tabella.insert('' ,END,values = (lista[0],lista[1],lista[2],lista[3],lista[4]))
        
    f.close()
#aggiungo la funzione alla menubar    
file_menu.add_command(label = 'Apri', command = apri_file)


root.mainloop()
