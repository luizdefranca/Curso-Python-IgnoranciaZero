from tkinter import Label, Entry, Canvas, Button, messagebox, Tk, N, W, E, S, Frame
from time import localtime, sleep

try:
    import winsound
except ImportError:
    import os
    def playsound(frequency,duration):
        #apt-get install beep
        os.system('beep -f %s -l %s' % (frequency,duration))
else:
    def playsound(frequency,duration):
        winsound.Beep(frequency,duration)

class Despertador:
    def __init__(self,raiz):
        self.root = raiz
        self.root.title('Despertador')

        self.frame = Frame(raiz)
        self.frame.pack()

        raiz = self.frame
 
        #Primeiro definimos as entradas de horas
        self.h_l = Label(raiz, text = 'Hora: ')
        self.h_e = Entry(raiz)
        self.h_l.grid(row = 0, column = 0)
        self.h_e.grid(row = 0, column = 1)

        #Minutos
        self.m_l = Label(raiz, text = 'Minuto: ')
        self.m_e = Entry(raiz)
        self.m_l.grid(row = 1, column = 0)
        self.m_e.grid(row = 1, column = 1)

        #Colocamos um canvas na lateral para representar a hora atual
        self.canvas = Canvas(raiz, width=200, height=100)
        self.canvas.grid(row = 0, column = 2, rowspan = 2, columnspan = 2, sticky = N+W+E+S)

        self.altura = 100 # Altura do canvas

        # Desenho do relógio-----------------------------
        pol=self.canvas.create_polygon
        ret=self.canvas.create_rectangle
        self.texto=self.canvas.create_text
        self.fonte=('BankGothic Md BT','20','bold')
        pol(10, self.altura-10, 40, self.altura-90, 160, self.altura-90, 190, self.altura-10, fill='darkblue')
        pol(18, self.altura-15, 45, self.altura-85, 155, self.altura-85, 182, self.altura-15, fill='dodgerblue')
        ret(45, self.altura-35, 90, self.altura-60, fill='darkblue', outline='')
        ret(110, self.altura-35, 155, self.altura-60, fill='darkblue', outline='')
        self.texto(100, self.altura-50, text=':', font=self.fonte, fill='yellow')
        # Fim do desenho do relógio-----------------------
        
        fonte = ('Comic Sans MS', '11', 'bold')

        #Botão que seta horário
        self.set = Button(raiz, text = 'Set', command=self.mostra, font = fonte, fg='darkblue', bg='deepskyblue')
        self.set.grid(row = 3, column = 0, columnspan = 2, sticky = N+W+E+S)

        #Botão que cancela o despertador
        self.cancel=Button(raiz, text='Cancela', command=self.cancel, font=fonte, fg='darkblue', bg='deepskyblue')
        self.cancel.grid(row = 3, column = 2, columnspan = 2, sticky = N+W+E+S)
        self.cancelado = False

        #Campo que atualiza tempo até toque do despertador
        self.tempo = Label(raiz, font = fonte, fg = 'black')

    def atualizaDespertador(self, HORA = "", MINUTO = ""):
        """
        Atualiza os campos do despertador
        """
        self.texto(67.5, self.altura-50, text=HORA, fill='yellow', font=self.fonte, tag='digitos_HORA')
        self.texto(132.5, self.altura-50, text=MINUTO, fill='yellow', font=self.fonte, tag='digitos_MIN')

    def atualizaCountdown(self, HORA, MINUTO):
        """
        Atualiza o label com o tempo até o despertar
        """
        h = self.HORA - HORA
        if h < 0:
            h += 24

        m = self.MINUTO - MINUTO
        if m < 0:
            m+=60

        self.tempo['text'] = "Tempo até Alarme: %.2i:%.2i"%(h, m)

    def mostra(self):
        """
        Atualiza Horário do despertador
        """
        try:
            self.HORA = int(self.h_e.get())
            self.MINUTO = int(self.m_e.get())
        except (TypeError, ValueError) as E:
            messagebox.showerror("Entrada Inválida", "A entrada de horário colocada é inválida")
        except Exception as E:
            messagebox.showerror("Erro",str(E))
        else:
            self.canvas.delete('digitos_HORA')
            self.canvas.delete('digitos_MIN')

            self.atualizaDespertador("%.2i"%self.HORA, "%.2i"%self.MINUTO)

            #Uma vez setado temos de tornar o botão não clicavel
            self.set['command'] = None
            self.set['bg'] = 'red'

            #Colocamos o label da atualização de horário
            HORA = int(str(localtime()[3]))
            MINUTO = int(str(localtime()[4]))
            self.atualizaCountdown(HORA, MINUTO)
            self.tempo.grid(row = 4, column = 0, columnspan = 4)

            #Por fim chamamos a função que conta as horas
            self.root.after(30, self.contando)
  
    def cancel(self):
        """
        Cancela o toque do alarme
        """
        self.canvas.delete('digitos_HORA')
        self.canvas.delete('digitos_MIN')

        self.HORA = self.MINUTO = ""
        self.atualizaDespertador()

        #Uma vez cancelado temos de tornar o botão clicavel
        self.set['command'] = self.mostra
        self.set['bg'] = 'deepskyblue'

        #Apagamos o tempo
        self.tempo.grid_forget()

        self.cancelado = True


    def contando(self):
        """
        Função que conta o tempo até o despertador
        """
        if not self.cancelado:
            HORA = int(str(localtime()[3]))
            MINUTO = int(str(localtime()[4]))
            if self.HORA == HORA and self.MINUTO == MINUTO:
                self.tempo.grid_forget()
                self.tocar()
            else:
                self.atualizaCountdown(HORA, MINUTO)
                self.root.after(30, self.contando)
        else:
            self.cancelado = False

    def tocar(self):
        """
        Toca o alarme
        """
        #winsound.PlaySound("som_test.wav", winsound.SND_FILENAME|winsound.SND_NOWAIT|winsound.SND_NODEFAULT|winsound.SND_ASYNC)
        for i in range(1,5):
            for j in range(1,5):
                playsound(100*j*i,100)
                sleep(0.01)
            sleep(0.01)
        

if __name__ == '__main__':
    instancia=Tk()
    Despertador(instancia)
    instancia.mainloop()
