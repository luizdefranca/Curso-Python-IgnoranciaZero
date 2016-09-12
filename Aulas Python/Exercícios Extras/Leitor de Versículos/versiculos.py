from tkinter import *

class Programa(object):
    def __init__(self, root):
        self.root = root
        self.label_frame = Frame(self.root)
        self.button_frame = Frame(self.root)

        self.cont = 0
        self.versiculos = ["Primeiro", "Segundo", "Terceiro"]
        self.max = len(self.versiculos)
        
        self.label = Label(self.label_frame, text = self.versiculos[self.cont])
        self.label.pack()
        
        self.anterior = Button(self.button_frame, text = "Anterior", command = self.volta)
        self.anterior["state"] = DISABLED
        self.anterior.pack(side = LEFT)
        
        self.proximo = Button(self.button_frame, text = "Proximo", command = self.avança)
        self.proximo.pack(side = LEFT)

        self.label_frame.pack()
        self.button_frame.pack()

    def volta(self):
        self.cont -= 1
        if self.cont == 0:
            self.anterior["state"] = DISABLED
        else:
            self.proximo["state"] = NORMAL

        self.label["text"] = self.versiculos[self.cont]

    def avança(self):
        self.cont += 1
        if self.cont == self.max - 1:
            self.proximo["state"] = DISABLED
        else:
            self.anterior["state"] = NORMAL

        self.label["text"] = self.versiculos[self.cont]

if __name__ == "__main__":
    r = Tk()

    p = Programa(r)

    r.title("Leitor de Versículos")

    r.geometry = ("800x600")
    r.resizable(False, False)
    r.minsize(width = 800, height = 600)

    r.mainloop()
    
