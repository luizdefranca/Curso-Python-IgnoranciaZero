from tkinter import *

class Calculadora(object):
    def __init__(self, instancia):
        #Colocar a entrada de texto
        self.form = Entry(instancia)
        self.form.pack()

        #Botão calcular
        self.calc = Button(instancia, text = "Calcule", command = self.Calcular)
        self.calc.pack()

        #Texto das formulas
        self.resultado = Label(instancia, text ="Resultado", fg = "blue")
        self.resultado.pack()

        botões = ('Comb(n, k)', 'binomial(n, x, p)', 'poisson(l, x, t)', 'soma(n, p, maior, menor = 0)', 'media', 'desvio', 'moda', 'mediana', 'variancia', 'p(x > k)', 'p(x >= k)', 'p(x < k)', 'p(x <= k)', 'p(k1 < x < k2)', 'p(k1 <= x < k2)', 'p(k1 < x <= k2)', 'p(k1 <= x <= k2)')

        for b in botões:
            a = Button(instancia, text = b, bg = 'green')
            a.pack()

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

#Dá um ícone ao aplicativo
#instancia.wm_iconbitmap('icone.ico')

#Inicia o programa
instancia.mainloop()
