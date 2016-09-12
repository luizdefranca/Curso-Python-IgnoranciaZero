#3) Posições
    #--> winfo.root
    #--> winfo.pointer

from tkinter import *
class Palheta:
    def __init__(self,raiz):
        raiz.title('Palheta Gráfica')
        self.canvas=Canvas(raiz, width=200, height=200)
        self.canvas.bind('<1>', self.misturar)
        self.canvas.pack()
        bola = self.canvas.create_oval
        bola(20,180,70,130, fill='red', outline='')
        bola(75,180,125,130, fill='green', outline='')
        bola(130,180,180,130, fill='blue', outline='')
        bola(45, 120, 155, 10, fill='white', outline='', tag='bola')
        self.tom=[0,0,0]

    def misturar(self, event):
        xo=self.canvas.winfo_rootx()
        yo=self.canvas.winfo_rooty()
        xa=self.canvas.winfo_pointerx()
        ya=self.canvas.winfo_pointery()
        cor=self.canvas.find_closest(xa-xo, ya-yo)[0]
        self.tom[cor-1] = self.tom[cor-1]+10
        cor="#%02x%02x%02x" %(self.tom[0], self.tom[1], self.tom[2])
        self.canvas.delete('bola')
        self.canvas.create_oval(45, 120, 155, 10, fill=cor, outline='', tag='bola')

inst = Tk()
Palheta(inst)
inst.mainloop()
