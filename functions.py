import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import os

#função para conexão num banco de dados sqlite3
def criarConexao():
    path = "C:\\Users\\Matheus\\Documents\\projetoBOLETIM\\banco\\boletimDB.db"
    con = None
    try:
        con = sqlite3.connect(path)
    except Error as ex:
        print(ex)
    return con

def select(sql):
    conexao = criarConexao()
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

def resetar():
    r = messagebox.askquestion("AVISO!!", "APAGAR TODOS OS DADOS DE ALUNOS?")
    if r != "yes":
        return
    else:
        try:
            c=criarConexao()
            c.execute("DELETE FROM tb_boletim")
            c.commit()
            c.close()
        except Error as ex:
            print(ex)

def deletar(treeView):
    r = messagebox.askquestion("AVISO!", "DELETAR ESTE ALUNO DO BANCO DE DADOS?")
    if (r == "no"):
        return
    else:
        try:
            line = treeView.selection()[0]
            vline = str(treeView.item(line)['values'][0])
            c=criarConexao()
            cursor = c.cursor()
            cursor.execute("DELETE FROM tb_boletim WHERE N_MATRICULA = '"+str(vline)+"' ")
            print(vline)
            c.commit()
            c.close()
            print("aluno excluido")
        except Error as ex:
            print(ex)

def limpar(n, n1, n2):
    n.delete(0, 'end')
    n1.delete(0, 'end')
    n2.delete(0, 'end')
    n.focus_set()


def consultarColuna():
    try:
        sql = "SELECT COUNT(*) from tb_boletim"
        con = criarConexao()
        cursor = con.cursor()
        cursor.execute(sql)
        resultado=cursor.fetchall()
        print ("tens um total de: ", resultado[0][0], "alunos")
        return resultado[0][0]
    except Error as ex:
        print(ex)

def novoCadastro():
    pastaApp=os.path.dirname(__file__)
    exec(open(pastaApp+"\\menuCadastro.py").read())
    
#vai ler o arquivo de texto com a matricula selecionada no treeview do maincode
def lerArquivo():
    arquivo = open("arquivo.txt", "r")
    vArquivo = arquivo.read()
    print("esta é a matricula no arquivo de texto: ",vArquivo)
    return vArquivo

def selectVariado():
    matri = lerArquivo()
    con = criarConexao()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tb_boletim WHERE N_MATRICULA = '"+matri+"'")
    resultado=cursor.fetchall()[0][0]
    print("matricula no banco de dados: ",resultado, "     classe da variavel da matricula", type(resultado))
    return resultado
    
# ssql = "SELECT * FROM tb_boletim"
# res = functions.select(vcon, ssql)
# cont = 0
# for r in res:
#     cont += 1
#     Label(wn, text=r[1]).grid(column=0, row=5+cont)