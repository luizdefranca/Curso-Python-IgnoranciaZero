from tkinter import *

AZUL = '#91B4FF'

#xbm, ppm, pgm, gif

class Calculadora(object):
    def __init__(self, instancia):
        self.font = ('Verdana', '20', 'bold')
        self.font2 = ('Verdana', '14', 'bold')

        logo = PhotoImage(file = 'Imagens/bg_python.gif')

        #Frame que contem os checkbuttons
        self.frame1 = Frame(instancia)
        self.frame1['bg'] = AZUL

        #Frame que contem a entrada de texto
        self.frame2 = Frame(instancia)
        self.frame2['bg'] = AZUL

        #Frame que contem o botão calcular
        self.frame3 = Frame(instancia)
        self.frame3['bg'] = AZUL

        #Frame que contem o texto das formulas
        self.frame4 = Frame(instancia, pady = 20)
        self.frame4['bg'] = AZUL

        #Frame que contem os botões especificos
        self.frame5 = Frame(instancia)
        self.frame5['bg'] = AZUL

        #Empacotamos as nossas frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        #Logo do aplicativo
        self.logo = Label(self.frame1)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        #Colocar a entrada de texto
        self.form = Entry(self.frame2)
        self.form.pack()

        #Botão calcular
        self.calc = Button(self.frame3, text = "Calcule", bg = "#A3FF65",command = self.Calcular, font = self.font)
        self.calc.pack()

        #Texto das formulas
        self.resultado = Label(self.frame4, text ="Resultado", fg = "blue", font = self.font2)
        self.resultado.pack()

        botões = ('Comb(n, k)', 'binomial(n, x, p)', 'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)', 'media', 'desvio', 'moda', 'mediana', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)')
        
        for i in range(len(botões)):
            if i % 3 == 0:
                 subframe = Frame(self.frame5)
                 subframe.pack()
            a = Button(subframe, text = botões[i], bg = 'green', width = 25, padx = 5)
            a.pack(side = LEFT)

        self.delete = Button(subframe, text = 'del', bg = 'red', width = 25, padx = 5)
        self.delete.pack(side = LEFT)

    def Calcular(self):
        self.resultado['text'] = self.form.get()
        self.resultado['fg'] = 'green'

#Cria a nossa tela
instancia = Tk()

#Criamos uma instancia da calculadora
Calculadora(instancia)

#Dá um título a tela
instancia.title('Calculadora para Estatística')

#Dá um tamanho a tela
instancia.geometry("800x600")

#Definir cor de background
instancia['bg'] = '#91B4FF'

#Dá um ícone ao aplicativo
#instancia.wm_iconbitmap('icone.ico')

#Inicia o programa
instancia.mainloop()
