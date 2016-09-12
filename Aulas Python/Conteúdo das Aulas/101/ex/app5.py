from tkinter import *

class Carinha2:
    def __init__(self, raiz):
        self.root = raiz

        self.canvas=Canvas(self.root, height=200, width=200, takefocus=1, bg='deepskyblue', highlightthickness=0)
        self.canvas.bind('<Left>', self.esquerda)
        self.canvas.bind('<Right>', self.direita)
        self.canvas.bind('<Up>', self.cima)
        self.canvas.bind('<Down>', self.baixo)
        self.canvas.focus_force()
        self.canvas.pack()
        
        # Desenho da carinha----------------------------------
        self.canvas.create_oval(90, 90, 110, 110, tag='bola', fill='yellow')
        self.canvas.create_oval(93, 100, 98, 95,tag='bola', fill='blue')
        self.canvas.create_oval(102, 100, 107, 95,tag='bola', fill='blue')
        self.canvas.create_arc(92, 87, 108, 107, tag='bola', start=220, extent=100, style=ARC)

    def esquerda(self, event): self.canvas.move('bola', -10, 0)
    def direita(self, event): self.canvas.move('bola', 10, 0)
    def cima(self, event): self.canvas.move('bola', 0, -10)
    def baixo(self, event): self.canvas.move('bola', 0, 10)
