from tkinter import *
from constantes import *

from retangulo import Retangulo
from bola import Bola
import random

#Binding
#<Motion> = Evento para o movimento do Mouse


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
        self.frame.pack();
        
        #Criamos a tela do jogo
        self.canvas = Canvas(self.frame, bg="black",width=CANVAS_L,height=CANVAS_A)
        self.canvas.pack()

        #E colocamos um botã para começar o jogo
        self.começar = Button(self.root, text = 'START', command = self.começa)
        self.começar.focus_force()
        self.começar.pack()

        #Bind com a tecla enter
        self.começar.bind('<Return>', self.começa)

        self.novoJogo()

        self.root.mainloop()


    def novoJogo(self):
        """
        Cria os elementos necessário para um novo jogo
        """
        #Criamos a bola que irá se movimentar
        self.bola = Bola(raio = 30, cor = 'red', pos = (100, 200), vel = (3, 3))

        #E o player tambem
        self.player = Retangulo(largura = 100, altura = 20, cor = 'green', pos = (LARGURA//2 + 100, 350), vel = (15, 15), tag = 'player')
        self.player.desenhar(self.canvas)

        #E adicionamos o evento de movimentação com o uso do teclado para o player
        self.canvas.bind('<Motion>', self.move_player)

        #Lista dos retângulos
        self.r = []

        #E por fim as diversas fileiras de retângulos
        l, c, e = 5, 8, 2 #linhas, colunas e espaçamento
        b, h, y0 = 48, 20, 50 #Base, altura e posição inicial dos retângulos
        for i in range(l):
            cor = random.choice(['green', 'orange', 'white', 'lightgray', 'yellow', 'purple'])
            for j in range(c):
                r = Retangulo(b, h, cor, (b*j+(j+1)*e, i*h+(i+1)*e + y0), (0, 0), 'rect')
                self.r.append(r)

        #Mantemos uma variável para mostrar que ainda está rolando um jogo
        self.jogando = True

    def começa(self, event):
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

    def move_player(self, event):
        """
        Move o player na tela de acordo com o movimento do mouse
        """
        if event.x > 0 and event.x < CANVAS_L - self.player.b:
            self.player.x = event.x

    def update(self):
        """
        Updatamos as condições do jogo
        """
        self.bola.update(self)

        #Depois de mover a bola é preciso procurar por colisões
        #self.VerificaColisão()

    def desenhar(self):
        """
        Método para redesenhar a tela do jogo
        """
        #primeiro apagamos tudo que há no canvas
        self.canvas.delete(ALL)

        #e o player
        self.player.desenhar(self.canvas)

        #E por fim todos os retângulos
        for r in self.r:
            r.desenhar(self.canvas)

        #depois desenhamos a bola
        self.bola.desenhar(self.canvas)

    def VerificaColisão(self):
        """
        Verifica se houve alguma colisão entre elementos do jogo
        """
        #Primeiro criamos uma bounding box para a bola
        coord = self.canvas.bbox('bola')
        #x1, y1, x2, y2

        #Depois pegamos a id de todos os objetos que colidem com a bola
        colisoes = self.canvas.find_overlapping(*coord)

        #Se o número de colisões for diferente de zero
        if len(colisoes) != 0:
            #verificamos se o id do objeto é diferente do player
            if colisoes[0] != self.player:
                #Vamos checar a colisão com o objeto mais próximo do topo
                #esquerdo da bola
                m_p = self.canvas.find_closest(coord[0], coord[1])
                
                #Depois temos que olhar para cada um dos retângulos para identificar
                #com quem a bola colidiu
                for r in self.r:
                    #tendo encontrado o retângulo
                    if r == m_p[0]:
                        #deletamos ele do jogo
                        self.r.remove(r)
                        self.canvas.delete(r)

                        #E invertemos o sentido da velocidade da bola
                        self.b_vy *= -1

                        #Por fim saimos da função 
                        return



if __name__ == '__main__':
    Jogo()
