from tkinter import *
NUM_IMAGENS = 4

def subimagem(imagem, x1, y1, x2, y2):
   """
   Com essa função, se tivessemos uma imagem única
   poderíamos separar cada uma das imagens
   por meio dela
   """
   dst = PhotoImage()
   dst.tk.call(dst, 'copy', imagem, '-from', x1, y1, x2, y2, '-to', 0, 0)
   return dst

class Mario:
    def __init__(self, root):
        self.root = root
        self.root.title('Mario')

        #Primeiro abrimos o spritesheet
        self.spritesheet = []
        sheet1 = []
        sheet2 = []
        for i in range(1, 5):
            sheet1.append(PhotoImage(file = 'Imagens/mario/mario_%i.ppm'%i))
            sheet2.append(PhotoImage(file = 'Imagens/mario/mario_l%i.ppm'%i))

        self.spritesheet.append(sheet1)
        self.spritesheet.append(sheet2)

        #Para o caso de uma imagem única com todas
        #as sprites dentro poderíamos extraí-las dessa forma
        #self.imagens = []
        #for i in range(4):
        #    sub = subimagem(self.spritesheet, i*28, 0, (i+1)*28, 18)
        #    self.imagens.append(sub)

        #Variavel que contem o número da imagem
        self.num_imagem = 3
        self.limite = 0

        #E colocamos a posição do mario
        self.x, self.y = 100, 71
        self.p = False
        self.m_vx = 10
        self.vx = 0
        self.d = 0
        self.moveu = True

        #self.root.after(10, self.andar)
      
        #configuramos o canvas
        self.canvas=Canvas(self.root, height=100, width=200, takefocus=1, bg='black', highlightthickness=0)
        self.canvas.bind('<Left>', self.esquerda)
        self.canvas.bind("<KeyRelease-Left>", self.solta)
        self.canvas.bind("<KeyRelease-Right>", self.solta)
        self.canvas.bind('<Right>', self.direita)
        self.canvas.focus_force()
        self.canvas.pack()

        #E colocamos um botã para começar o jogo
        self.começar = Button(self.root, text = 'START', command = self.começa)
        self.começar.focus_force()
        self.começar.pack()

        self.root.mainloop()

    def esquerda(self, event): 
        self.vx = -self.m_vx
        self.d = 1
        self.p = True
    def direita(self, event): 
        self.vx = self.m_vx
        self.d = 0
        self.p = True
    def solta(self, event):
        self.p = False

    def começa(self):
        """
        Inicia o jogo
        """
        self.andar()

    def andar(self):
        """
        Deve ser executado enquanto o jogo estiver rodando
        """
        if self.p:
            if 0 < self.x < 184:
                self.x += self.vx
            if self.x > 184:
                self.x = 183
            if self.x < 16:
                self.x = 17
        
            self.num_imagem -= 1
            if self.num_imagem < 0:
                self.num_imagem = 3
        else:
            self.num_imagem = 3

        self.canvas.delete(ALL)

        self.canvas.focus_force()

        self.canvas.create_image((self.x, self.y), image = self.spritesheet[self.d][self.num_imagem])
        
        self.root.after(70, self.andar)
         
        

    def desenha(self):
        self.num_imagem += 1


if __name__ == '__main__':
    r = Tk()
    Mario(r)
