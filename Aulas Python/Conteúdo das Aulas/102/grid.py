"""
Aula de Finalização do tema do tkinter
"""

#1) Métodos de Tk()
    #--> minsize
    #--> maxsize

#2) Grid
    #--> widget.grid(row = linha, column = coluna) (posição do widget)
    #--> columnspan/rowspan = colunas/linhas que ele pode ocupar
    #--> sticky = N/W/E/S = posicionamento do widget com relação a uma célula
    #--> pad
    #--> grid_forget(pack_forget)

from tkinter import *

class Imagem(object):
    def __init__(self, root):
        """
        Método construtor da classe imagem
        """
        #Primeiro selecionamos o root
        self.root = root

        #Depois criamos o label altura
        self.a = Label(self.root, text="Altura: ")
        self.a.grid(row = 0, sticky=E)
    
        #E o label largura
        self.l = Label(self.root, text="Largura: ")
        self.l.grid(row = 1, sticky=E)

        #Criamos as duas entradas para dados
        self.e1 = Entry(self.root)
        self.e2 = Entry(self.root)
        self.e1.grid(row = 0, column = 1)
        self.e2.grid(row = 1, column = 1)

        #O botão que verifica se deve-se ou não preservar o aspecto
        self.p = Checkbutton(self.root, text = "Preserva Aspecto")
        self.p.grid(columnspan=2, sticky=W)
        self.prv = False

        #E a imagem que nós devemos colocar
        self.imagem = Label(self.root)
        self.img = PhotoImage(file = 'img.ppm').subsample(1, 1)
        self.zoomimg = self.img
        self.imagem['image'] = self.zoomimg
        self.imagem.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

        #Por fim colocamos o botões de zoomIn
        self.rI = Button(self.root, text = 'Zoom In', command = self.zoomIn)
        self.rI.grid(row=2, column=2)
    
        #E zoom out
        self.rO = Button(self.root, text = 'Zoom Out', command = self.zoomOut)
        self.rO.grid(row=2, column=3)

        #E as variaveis relativas a zoom
        self.zoom = 1
        self.zoomimg = self.img

    def zoomIn(self):
        """
        Dá um zoom na imagem
        """
        if self.zoom < 8:
            self.zoom += 1
        self.zoomimg = self.img.zoom(self.zoom, self.zoom)
        self.imagem['image'] = self.zoomimg

    def zoomOut(self):
        """
        Se afasta da imagem
        """
        if self.zoom > 1:
            self.zoom -= 1
        self.zoomimg = self.img.zoom(self.zoom, self.zoom)
        self.imagem['image'] = self.zoomimg


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x100")
    root.minsize(width = 400, height = 100) #tamanho minimo
    root.maxsize(width = 600, height = 400) #tamanho maximo
    root.title('Final')
    img = Imagem(root)
    root.mainloop()
