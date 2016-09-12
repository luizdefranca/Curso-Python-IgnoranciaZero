def Entra():
    """
    Função lida com a tentativa do usuário
    de tentar logar verificando se o usuário
    se encontra no database e se sua senha está
    correta e devolve uma mensagem adequada
    """
    global db, u_e, s_e, m_l
    usuario = u_e.get()
    senha = s_e.get()

    if usuario not in db:
        m_l["text"] = "Usuário Inválido"
        m_l["fg"] = "red"
    else:
        if senha == db[usuario]:
            m_l["text"] = "Bem vindo %s"%usuario
            m_l["fg"] = "blue"
        else:
            m_l["text"] = "Senha Inválida"
            m_l["fg"] = "red"

#Importamos o módulo do tkinter
from tkinter import *

#importamos o shelve para lidar com o database
import shelve

#Inicializamos a nossa janela
i = Tk()

#Colocamos um titulo nela
i.title("Login")

#Definimos sua geometria
i.geometry = ("400x300")

#Depois criamos o label do usuário
u_l = Label(i, text = "Usuário")

#Colocamos a entry do campo usuário
u_e = Entry(i)

#Colocamos a label da senha
s_l = Label(i, text = "Senha")

#E a entry da senha
s_e = Entry(i)

#Criamos o botão de entrar
e = Button(i, text = 'Entrar', command = Entra)

#E a label que vai devolver uma msg para o usuário
m_l = Label(i, text = "")

#Empacotamos os widgets
u_l.pack()
u_e.pack()
s_l.pack()
s_e.pack()
e.pack()
m_l.pack()

#Abrimos os databases com as senhas
db = shelve.open("login.db")

i.mainloop()

