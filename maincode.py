from sqlite3 import Error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functions import *
from functions import select


#função para abrir nova janela
# pastaApp=os.path.dirname(__file__)
# def novoCadastro():
#     exec(open(pastaApp+"\\menuCadastro.py").read())

#escreve a matricula selecionada num arquivo de texto


#atualiza a treeview
def refreshTable():
    for data in treeView.get_children():
        treeView.delete(data)
    for array in select("SELECT * from tb_boletim"):
        treeView.insert(parent='', index='end', iid=array, text="", values=(array), tag='orow')
    treeView.tag_configure('orow', font=('Arial', 12))
    treeView.grid(column=0, row=1, padx=10, pady=20)

def cadastrar(conexao):
    n = nome.get()
    matri = matricula.get()
    vcpf = cpf.get()
    if (n == "" or n == " "):
        messagebox.showinfo("ERRO", "O NOME DO ALUNO NÃO PODE ESTAR VAZIO")
        return
    else:
        vsql = "INSERT INTO tb_boletim (N_MATRICULA, T_NOMEALUNO, T_CPF) VALUES ('"+matri+"', '"+n+"', '"+vcpf+"')"
        try:
            c=conexao.cursor()
            c.execute(vsql)
            conexao.commit()
            print("aluno inserido")
            refreshTable()
        except Error as ex:
            print(ex)
            
def consultarTreeview(mtreeView):        
    linha = mtreeView.selection()[0]
    mar = mtreeView.item(linha)['values'][0]
    print(mar)
    escreverArquivo(mar)
    return mar

def escreverArquivo(matr):
    arquivo = open("arquivo.txt", "w")
    vArquivo = arquivo.write(str(matr))
    return vArquivo

def defatualizar(nota1, nota2, nota3, nota4, name, bcpf):
    matri = consultarTreeview(treeView)
    not1 = nota1.get()
    not2 = nota2.get()
    not3 = nota3.get()
    not4 = nota4.get()
    bname = name.get()
    cepeefi = bcpf.get()
    con = criarConexao()
    cursor = con.cursor()
    cursor.execute("UPDATE tb_boletim SET T_NOMEALUNO='"+
        bname+"', T_NOTAUM='"+str(not1)+"', T_NOTADOIS='"+
        str(not2)+"', T_NOTATRES='"+str(not3)+"', T_NOTAQUATRO='"+
        str(not4)+"', T_CPF='"+cepeefi+"' WHERE N_MATRICULA = '"+str(matri)+"'")
    con.commit()
    con.close()

def janelaBoletim():
    bmatricula = consultarTreeview(treeView)
    print(bmatricula)
    dados = select("SELECT * FROM tb_boletim WHERE N_MATRICULA = '"+str(bmatricula)+"'")
    bnome = dados[0][1]
    bcpf = dados[0][2]
    n1 = dados[0][3]
    n2 = dados[0][4]
    n3 = dados[0][5]
    n4 = dados[0][6]
    
    window = Tk()
    window.geometry("425x150")

    Label(window, text="Nome").place(x=45, y=1)
    namo = Entry(window)
    namo.place(x=5, y=20)
    namo.insert(0, bnome)

    Label(window, text="Matricula").place(x=180, y=1)
    Matr = Entry(window)
    Matr.place(x=145, y=20)
    Matr.insert(0, bmatricula)

    Label(window, text="CPF").place(x=335, y=1)
    vcpf = Entry(window)
    vcpf.place(x=285, y=20)
    vcpf.insert(0, bcpf)

    Label(window, text="Nota B1").place(x=45, y=40)
    b1 = Entry(window)
    b1.place(x=5, y=60)
    b1.insert(0, n1)

    Label(window, text="Nota B2").place(x=180, y=40)
    b2 = Entry(window)
    b2.place(x=145, y=60)
    b2.insert(0, n2)

    Label(window, text="Nota B3").place(x=45, y=80)
    b3 = Entry(window)
    b3.place(x=5, y=100)
    b3.insert(0, n3)

    Label(window, text="Nota B4").place(x=180, y=80)
    b4 = Entry(window)
    b4.place(x=145, y=100)
    b4.insert(0, n4)

    atualizar = ttk.Button(window, text="Atualizar", command=lambda: defatualizar(b1, b2, b3, b4, namo, vcpf))
    atualizar.place(x=283, y=50) #nota1, nota2, nota3, nota4, name, bcpf

    window.mainloop()

#criacao da janela em tkinter
wn = Tk()
wn.title("Sistema de Boletim")
wn.geometry("400x300")

treeView = ttk.Treeview(wn)

style = ttk.Style()
style.configure("Treeview.Heading")

treeView['columns'] = ("Matricula", "Nome")

treeView.column("#0", width=0, stretch=NO)
treeView.column("Matricula", anchor=W, width=100)
treeView.column("Nome", anchor=W, width=80)


treeView.heading("Matricula", anchor=W, text="Matricula")
treeView.heading("Nome", anchor=W, text="Nome")

refreshTable()

Label(wn, text="Alunos cadastrados:").grid(column=0, row=0)


#cria conexao com o banco de dados
vcon=criarConexao()

#entry do nome do aluno
Label(wn, text="Nome do aluno:").place(x=285, y=2)
nome = Entry(wn)
nome.place(x=270, y=20)

#entry da primeira nota do aluno
Label(wn, text="Matricula:").place(x=310, y=40)
matricula = Entry(wn)
matricula.place(x=270, y=60)

#entry da segunda nota do aluno
Label(wn, text="CPF:").place(x=310, y=80)
cpf = Entry(wn)
cpf.place(x=270, y=100)

#botão para adicionar novo aluno
adicionar = ttk.Button(wn, text="Adicionar novo aluno", command=lambda: [cadastrar(vcon), limpar(nome, matricula, cpf)])
adicionar.place(x=270, y=130)

#botão para abrir nova janela com dados do aluno selecinado na treeview
abrir = ttk.Button(wn, text="Selecionar aluno", command=janelaBoletim)
abrir.place(x=270, y=160)

#botão para remover aluno
remover = ttk.Button(wn, text="Remover aluno", command=lambda: [deletar(treeView), refreshTable()])
remover.place(x=270, y=190)

#botão que apaga todos os dados do banco de dados
resetar = ttk.Button(wn, text="Apagar tudo", command=lambda:[resetar(), refreshTable()])
resetar.place(x=270, y=220)

#botão de teste que vai printar no console os dados da linha selecionada no treeview
printar = ttk.Button(wn, text="contar alunos", command=lambda:[consultarColuna()])
printar.place(x=8, y=270)

#fecha a janela do boletim
fechar = ttk.Button(wn, text="fechar boletim", command=wn.destroy)
fechar.place(x=270, y=280)

wn.mainloop()