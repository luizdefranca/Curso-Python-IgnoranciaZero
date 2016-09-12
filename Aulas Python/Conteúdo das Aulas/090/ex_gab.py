#Importamos o módulo do tkinter
from tkinter import *

#importamos o shelve para lidar com o database
import shelve

class Entrada(object):
    def __init__(self, i):
        #Depois criamos o label do usuário
        self.u_l = Label(i, text = "Usuário")
        
        #Colocamos a entry do campo usuário
        self.u_e = Entry(i)

        #Colocamos a label da senha
        self.s_l = Label(i, text = "Senha")

        #E a entry da senha
        self.s_e = Entry(i, show = '*')

        #Criamos o botão de entrar
        self.e = Button(i, text = 'Entrar', command = self.Entra)
        
        #E o botão de novo usuário
        self.n = Button(i, text = "Novo", command = self.Novo)

        #E a label que vai devolver uma msg para o usuário
        self.m_l = Label(i, text = "")

        #Empacotamos os widgets
        self.u_l.pack()
        self.u_e.pack()
        self.s_l.pack()
        self.s_e.pack()
        self.m_l.pack()
        self.e.pack(side = LEFT)
        self.n.pack(side = RIGHT)
        
 
        #Abrimos os databases com as senhas
        self.db = shelve.open("login.db")

        #E criamos a variável booleana identificando se estamos no modo criar ou não
        self.criar = False

    def MSG(self, msg, cor = 'red'):
        self.m_l["text"] = msg
        self.m_l["fg"] = cor
    
    def Entra(self):
        """
        Função lida com a tentativa do usuário
        de tentar logar verificando se o usuário
        se encontra no database e se sua senha está
        correta e devolve uma mensagem adequada
        """
        usuario = self.u_e.get()
        senha = self.s_e.get()

        if usuario not in self.db:
            self.MSG("Usuário Inválido")
        else:
            if senha == self.db[usuario]:
                self.MSG("Bem vindo %s"%usuario, cor = "blue")
            else:
                self.MSG("Senha Inválida")
    
    def Novo(self):
        """
        Faz as modificações necessárias para entrar no modo
        criar novo usuário e senha
        """
        if not self.criar:
            self.n['text'] = 'Criar'
            self.n['bg'] = 'black'
            self.n['fg'] = 'white'
            self.u_l['text'] = 'Nome de Usuário'
            self.u_l['fg'] = 'green'
            self.s_l['fg'] = 'green'
            self.criar = True
        else:
            self.Cria()
    
    def Cria(self):
        """
        Método usado para criar um novo usuário
        e uma senha
        """
        usuario = self.u_e.get()
        senha = self.s_e.get()

        if len(senha) == 0 or len(usuario) == 0:
            self.MSG("Nenhum dos campos pode estar vazio!")
        elif usuario in self.db:
            self.MSG("Usuário já existe!")
        else:
            self.db[usuario] = senha
            self.n['text'] = 'Novo'
            self.n['bg'] = 'lightgray'
            self.n['fg'] = 'black'
            self.u_l['text'] = 'Usuário'
            self.u_l['fg'] = 'black'
            self.s_l['fg'] = 'black'
            self.MSG('Usuário criado com sucesso', 'blue')
            self.criar = False
        


#Inicializamos a nossa janela
i = Tk()

#Inicializamos as variáveis do nosso programa
e = Entrada(i)

#Colocamos um titulo nela
i.title("Login")

#Definimos sua geometria
i.geometry = ("600x300")

i.mainloop()

