from tkinter import *

class Carinha:
    def __init__(self, raiz):
        self.root = raiz
        self.root.title('Carinha')
        self.canvas=Canvas(self.root, height=200, width=200, takefocus=1, bg='deepskyblue', highlightthickness=0)
        self.canvas.focus_force()
        self.canvas.pack()
        
        # Desenho da carinha----------------------------------
        self.canvas.create_oval(90, 90, 110, 110, tag='bola', fill='yellow')
        self.canvas.create_oval(93, 100, 98, 95,tag='bola', fill='blue')
        self.canvas.create_oval(102, 100, 107, 95,tag='bola', fill='blue')
        self.canvas.create_arc(92, 87, 108, 107, tag='bola', start=220, extent=100, style=ARC)

        self.vx = 5
        self.vy = 4
        self.x = 90
        self.y = 90

        #E colocamos um botã para começar o jogo
        self.começar = Button(self.root, text = 'START', command = self.começa)
        self.começar.pack()

    def começa(self):
        self.move()

    def move(self):
        self.canvas.move('bola', self.vx, self.vy)
        self.x += self.vx
        self.y += self.vy

        if self.x > 180 or self.x < 0:
            self.vx *= -1
        if self.y > 180 or self.y < 0:
            self.vy *= -1
        
        self.root.after(10, self.move)
