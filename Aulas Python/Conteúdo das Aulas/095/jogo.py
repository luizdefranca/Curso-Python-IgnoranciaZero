from tkinter import *
from constantes import *

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
        self.canvas = Canvas(self.frame, bg="black",width=CANVAS_L,height=CANVAS_A, cursor = 'watch')
        self.canvas.pack()

        self.canvas.create_line(0, 0, 100, 100, fill = 'white')

        #E colocamos um botã para começar o jogo
        self.começar = Button(self.root, text = 'START')
        self.começar.pack()

        #self.novoJogo()

        self.root.mainloop()

if __name__ == '__main__':
    Jogo()
