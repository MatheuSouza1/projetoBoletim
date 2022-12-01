from tkinter import *
from tkinter import ttk
from sqlite3 import *
from sqlite3 import Error
from functions import selectVariado
from functions import select

matricula = selectVariado()
print(matricula)
dados = select()
nome = dados[0][1]
cpf = dados[0][2]
n1 = dados[0][3]
n2 = dados[0][4]
n3 = dados[0][5]
n4 = dados[0][6]

print(f"nome:{nome} cpf: {cpf} notas: {n1}{n2}{n3}{n4}")
        
window = Tk()
window.geometry("425x150")

Label(window, text="Nome").place(x=45, y=1)
namo = Entry(window)
namo.place(x=5, y=20)
namo.insert(0, "Matheus")

Label(window, text="Matricula").place(x=180, y=1)
Matr = Entry(window)
Matr.place(x=145, y=20)
Matr.insert(0, matricula)

Label(window, text="CPF").place(x=335, y=1)
cpf = Entry(window)
cpf.place(x=285, y=20)
cpf.insert(0, "152.054.817-65")

Label(window, text="Nota B1").place(x=45, y=40)
b1 = Entry(window)
b1.place(x=5, y=60)
b1.insert(0, "6")

Label(window, text="Nota B2").place(x=180, y=40)
b2 = Entry(window)
b2.place(x=145, y=60)
b2.insert(0, "8")

Label(window, text="Nota B3").place(x=45, y=80)
b3 = Entry(window)
b3.place(x=5, y=100)
b3.insert(0, "5")

Label(window, text="Nota B4").place(x=180, y=80)
b4 = Entry(window)
b4.place(x=145, y=100)
b4.insert(0, "10")

atualizar = ttk.Button(window, text="Atualizar", command=None)
atualizar.place(x=283, y=50)

window.mainloop()