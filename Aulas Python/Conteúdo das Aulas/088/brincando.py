from tkinter import *

i = Tk()

i.title("Brincando")

i.geometry("400x300")

texto = Label(i, text = "Meu texto")
texto.pack()

ent = Entry(i)
ent.pack()

b = Button(i, text = "Clique")
b.pack()


i.mainloop()
