from tkinter import *

#Cria a nossa tela
instancia = Tk()

#Dá um título a tela
instancia.title('Calculadora para Estatística')

#Dá um tamanho a tela
instancia.geometry("800x600")

#Dá um ícone ao aplicativo
#instancia.wm_iconbitmap('icone.ico')

#Colocar a entrada de texto
form = Entry(instancia)
form.pack()

#Botão calcular
calc = Button(instancia, text = "Calcule")
calc.pack()

#Texto das formulas
resultado = Label(instancia, text ="Resultado", fg = "blue")
resultado.pack()

#Inicia o programa
instancia.mainloop()
