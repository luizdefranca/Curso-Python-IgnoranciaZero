#Importamos o módulo do tkinter
from tkinter import *

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

#Por fim criamos o botão de entrar
e = Button(i, text = 'Entrar')

#Empacotamos os widgets
u_l.pack()
u_e.pack()
s_l.pack()
s_e.pack()
e.pack()

i.mainloop()


