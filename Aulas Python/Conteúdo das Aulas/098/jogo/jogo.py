from tkinter import *
from constantes import *
import random

#Canvas: itemconfig, id, delete, tag, move
#Tk: after

class Jogo(object):
    """
    Classe que organiza os elementos do jogo
    """
    def __init__(self):
        #Criamos o conteiner principal do jogo
        self.root = Tk()
        self.root.geometry('%ix%i'%(LARGURA, ALTURA))
        self.root.resizable(False, False)
        self.root.title('Joguinho Besta')

        #E uma frame para conter o canvas
        self.frame=Frame(bg="black")
        self.frame.pack()
        
        #Criamos a tela do jogo
        self.canvas = Canvas(self.frame, bg="black",width=CANVAS_L,height=CANVAS_A, cursor = 'target')
        self.canvas.pack()

        #E colocamos um botã para começar o jogo
        self.começar = Button(self.root, text = 'START', command = self.começa)
        self.começar.pack()

        #self.canvas.create_polygon((100, 200), (150, 250), (250, 250), (300, 200), (300, 100), (250, 50), (150, 50), (100, 100), fill = 'white')

        self.novoJogo()

        self.root.mainloop()

    def novoJogo(self):
        """
        Cria os elementos de um novo jogo
        """
        self.player = self.canvas.create_rectangle((CANVAS_L//2, 350), (CANVAS_L//2 + 100, 370), fill = 'green')

        #Cria a bola do jogo
        raio = 30
        p = (100, 200)
        self.bola = self.canvas.create_oval(p[0],p[1], p[0] + raio, p[1] + raio, fill='red', outline='white', tag = 'bola')
        self.b_vx = self.b_vy = 5
        self.b_x, self.b_y = p

        #Cria um arco dentro da bola
        #self.canvas.create_arc(p[0], p[1], p[0] + raio, p[1] + raio, fill = 'orange', start = 60, tag = 'bola')#, extent = 90)

        #Lista dos retângulos
        self.r = []

        #E por fim as diversas fileiras de retângulos
        l, c, e = 5, 8, 2 #linhas, colunas e espaçamento
        b, h, y0 = 48, 20, 50 #Base, altura e posição inicial dos retângulos
        for i in range(l):
            cor = random.choice(['green', 'orange', 'white', 'lightgray', 'yellow', 'purple'])
            for j in range(c):
                self.canvas.create_rectangle(b*j+(j+1)*e, i*h+(i+1)*e + y0,b*j+(j+1)*e + b, i*h+(i+1)*e + y0 + h, fill = cor)

        #self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text = 'OLA COLEGA!', fill = 'white')

        self.jogando = True

    def começa(self):
        """
        Inicia o jogo
        """
        self.jogar()

    def jogar(self):
        """
        Deve ser executado enquanto o jogo estiver rodando
        """
        if self.jogando:
            self.update()
            self.desenhar()
            
            self.root.after(10, self.jogar)
         
        else:
            self.acabou(self.msg)


    def desenhar(self):
        """
        Método para redesenhar a tela do jogo
        """
        #self.canvas.delete('bola')
        #self.bola = self.canvas.create_oval(self.b_x, self.b_y, self.b_x + 30, self.b_y + 30, fill='red', outline='white', tag = 'bola')
        #self.canvas.create_arc(self.b_x, self.b_y, self.b_x + 30, self.b_y + 30, fill = 'orange', start = 60, tag = 'bola')
        pass

    def update(self):
        """
        Updatamos as condições do jogo
        """
        #self.canvas.itemconfig(self.player, fill = 'blue')
        self.canvas.move('bola', self.b_vx, self.b_vy)
        self.b_x += self.b_vx
        self.b_y += self.b_vy

        if self.b_x > CANVAS_L - 30 or self.b_x < 0:
            self.b_vx*=-1
        
        if self.b_y > CANVAS_A - 30 or self.b_y < 0:
            self.b_vy*=-1
        

        



if __name__ == '__main__':
    Jogo()
