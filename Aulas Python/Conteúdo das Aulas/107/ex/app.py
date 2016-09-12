import sys, os
from functools import partial

sys.path.append('apps')
for i in range(1, 10):
    sys.path.append('apps/app%i'%i)

#Importamos o módulo do tkinter
from tkinter import *
from app1 import Linhas
from app2 import SPFC
from app3 import Fatias
from app4 import Carinha
from app5 import Carinha2
from app6 import Mario
from app7 import Desenha
from app8 import Horas
from app9 import Despertador

AZUL = '#3784BA'

#importamos o shelve para lidar com o database
import shelve

class Entrada(object):
    def __init__(self, i):
        self.mestre = i
        self.font = ('Verdana', '36', 'bold')

        #Frame que contem as entradas de texto
        self.frame1 = Frame(i)
        self.frame1['background'] = AZUL

        #Frame que contem os botões
        self.frame2 = Frame(i)
        self.frame2['background'] = AZUL

        self.TelaPrincipal()
        
        #Abrimos os databases com as senhas
        self.db = shelve.open(os.path.join("database","login.db"))

        #E criamos a variável booleana identificando se estamos no modo criar ou não
        self.criar = False

        #E verificamos se devemos preencher os campos de texto com alguma coisa
        self.Preenxer()

    def TelaPrincipal(self):
        """
        Cria e impacota os elementos principais do aplicativo
        """
        self.novo = PhotoImage(file = os.path.join('Imagens','b_novo.ppm'))
        self.cria = PhotoImage(file = os.path.join('Imagens','b_criar.ppm'))

        imagens = PhotoImage(file = os.path.join('Imagens','bg_python.gif'))

        #Depois criamos o título
        self.titulo = Label(self.frame1)
        self.titulo.image = imagens
        self.titulo['image'] = imagens
        self.titulo.grid(row = 1, column = 1, columnspan = 2)
     
        self.Usuario_Senha()

        #Então criamos o checkbutton lembrar
        self.c_b = Checkbutton(self.frame1, font = self.font, text = 'Lembrar-me', bg = AZUL, command = self.Lembrar)
        self.c_b.grid(row = 5, column = 1, columnspan = 2)
        self.selecionado = False
        
        #Criamos o botão de entrar
        entrar = PhotoImage(file = os.path.join('Imagens','b_entrar.ppm'))
        self.e = Button(self.frame2, text = 'Entrar', command = self.Entra)
        self.e['image'] = entrar
        self.e.image = entrar

        #E o botão de novo usuário
        self.n = Button(self.frame2, text = "Novo", command = self.Novo)
        self.n['image'] = self.novo

        #Empacotamos os widgets
        self.EmpacotaTelaPrincipal()

    def Usuario_Senha(self):
        """
        Cria os campos de usuário e senha
        """
        #Depois criamos o label do usuário
        self.u_l = Label(self.frame1, text = "Usuário: ", font = self.font, bg = AZUL)
        self.u_l.grid(row = 2, column = 1, sticky = E)
        
        #Colocamos a entry do campo usuário
        self.u_e = Entry(self.frame1, font = self.font, width = 15)
        self.u_e.grid(row = 2, column = 2, sticky=W)

        #Colocamos a label da senha
        self.s_l = Label(self.frame1, text = "Senha: ", font = self.font, bg = AZUL)
        self.s_l.grid(row = 3, column = 1, sticky = E)

        #E a entry da senha
        self.s_e = Entry(self.frame1, show = '*', font = self.font, width = 15)
        self.s_e.grid(row = 3, column = 2, sticky = E)

        #E a label que vai devolver uma msg para o usuário
        self.m_l = Label(self.frame1, text = "")
        self.m_l.grid(row = 4, column = 1, columnspan = 2)

    def TelaSecundária(self):
        """
        Cria uma tela secundária para rodar os aplicativos
        """
        #Definimos as configurações de cada botão
        configurações = [('App Canvas 1 - Linhas', Linhas), ('App Canvas 2 - SPFC', SPFC),
                         ('App Canvas 3 - Fatias', Fatias), ('App Canvas 4 - Carinha', Carinha),
                         ('App Canvas 5 - Carinha 2', Carinha2), ('App Canvas 6 - Mario', Mario),
                         ('App Canvas 7 - Desenha', Desenha), ('App Canvas 8 - Horas', Horas),
                         ('App Canvas 9 - Despertador', Despertador)]

        #Criamos uma lista para todos os botões
        self.buttons = []

        #Colocamos cada botão na tela e a lista de botões
        for conf in configurações:
            b = Button(self.mestre, text = conf[0], command = partial(self.exec_app, conf[1]))
            b.pack(fill = BOTH, expand = True)
            self.buttons.append(b)

    def exec_app(self, command):
        """
        Função genérica que executa o aplicativo selecionado
        """
        self.destroiTelaSecundaria()
        command(self.mestre)

    def destroiTelaSecundaria(self):
        """
        Apaga todos os botões que constituem a tela secundária
        """
        for b in self.buttons:
            b.destroy()

    def EmpacotaTelaPrincipal(self):
        """
        Organiza os elementos da tela principal de maneira adequada
        """
        self.frame1.pack()
        self.frame2.pack()
        self.titulo.grid(row = 1, column = 1, columnspan = 2)
        self.c_b.grid(row = 5, column = 1, columnspan = 2)
        self.u_l.grid(row = 2, column = 1, sticky = E)
        self.u_e.grid(row = 2, column = 2, sticky=W)
        self.s_l.grid(row = 3, column = 1, sticky = E)
        self.s_e.grid(row = 3, column = 2, sticky = E)
        self.m_l.grid(row = 4, column = 1, columnspan = 2)
        self.e.pack(side = LEFT)
        self.n.pack(side = RIGHT)

    def DestroiTelaPrincipal(self):
        """
        Apaga os elementos da tela principal
        """
        self.frame1.destroy()
        self.frame2.destroy()
        self.titulo.destroy()
        self.u_l.destroy()
        self.u_e.destroy()
        self.s_l.destroy()
        self.s_e.destroy()
        self.c_b.destroy()
        self.m_l.destroy()
        self.e.destroy()
        self.n.destroy()

    def DesempacotaTelaPrincipal(self):
        """
        Esconde da tela todos os elementos da tela principal
        """
        self.titulo.grid_forget()
        self.u_l.grid_forget()
        self.u_e.grid_forget()
        self.s_l.grid_forget()
        self.s_e.grid_forget()
        self.c_b.grid_forget()
        self.m_l.grid_forget()
        self.e.pack_forget()
        self.n.pack_forget()

    def EmpacotaCria(self):
        self.l_nome.pack()
        self.e_nome.pack()
        self.l_email.pack()
        self.e_email.pack()
        self.u_l.pack()
        self.u_e.pack()
        self.s_l.pack()
        self.s_e.pack()
        self.b_criar.pack()
        self.m_l.pack()

    def DestroiCria(self):
        """
        Destroi elementos da tela de criar
        """
        self.l_nome.destroy()
        self.e_nome.destroy()
        self.l_email.destroy()
        self.e_email.destroy()
        self.b_criar.destroy()
        self.u_l.pack_forget()
        self.u_e.pack_forget()
        self.s_l.pack_forget()
        self.s_e.pack_forget()
        self.m_l.pack_forget()

    def Preenxer(self):
        if 'Lembrar' in self.db:
            self.u_e.insert(0, self.db['Lembrar']['Usuário'])
            self.s_e.insert(0, self.db['Lembrar']['Senha'])


    def MSG(self, msg, cor = 'red'):
        self.m_l["text"] = msg
        self.m_l["fg"] = cor

    def Lembrar(self):
        """
        Função que troca o estado da variável do checkbutton
        """
        self.selecionado = not self.selecionado
    
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
            if senha == self.db[usuario]['Senha']:
                self.MSG("Bem vindo %s"%usuario, cor = "blue")
                self.DestroiTelaPrincipal()
                self.TelaSecundária()
                if self.selecionado:
                    self.db['Lembrar'] = {'Usuário': usuario, 'Senha': senha}
            else:
                self.MSG("Senha Inválida")
    
    def Novo(self):
        """
        Faz as modificações necessárias para entrar no modo
        criar novo usuário e senha
        """
        self.DesempacotaTelaPrincipal()
        self.l_nome = Label(self.frame1, text = 'Nome', font = self.font, bg = AZUL)
        self.e_nome = Entry(self.frame1, font = self.font)
        self.l_email = Label(self.frame1, text = 'Email', font = self.font, bg = AZUL)
        self.e_email = Entry(self.frame1, font = self.font)
        self.b_criar = Button(self.frame1, image = self.cria, command = self.Cria)

        self.EmpacotaCria()
    
    def Cria(self):
        """
        Método usado para criar um novo usuário
        e uma senha
        """
        usuario = self.u_e.get()
        senha = self.s_e.get()
        nome = self.e_nome.get()
        email = self.e_email.get()

        if len(senha) == 0 or len(usuario) == 0 or len(nome) == 0 or len(email) == 0:
            self.MSG("Nenhum dos campos pode estar vazio!")
        elif usuario in self.db:
            self.MSG("Usuário já existe!")
        else:
            self.db[usuario] = {'Nome': nome, 'Email': email, 'Senha': senha}

            self.DestroiCria()

            self.u_e.delete(0, END)
            self.s_e.delete(0, END)

            self.EmpacotaTelaPrincipal()
           
            self.MSG('Usuário criado com sucesso', 'blue')
            
        


if __name__=='__main__':
    #Inicializamos a nossa janela
    i = Tk()

    #Inicializamos as variáveis do nosso programa
    e = Entrada(i)

    #Colocamos um titulo nela
    i.title("Login")
    i.bind('<Escape>', sys.exit)

    #Definimos sua geometria
    i.geometry = ("800x600")

    i.resizable(False, False)
    i.minsize(width = 800, height = 600)

    #Definimos uma cor de fundo
    i['background'] = AZUL

i.mainloop()

