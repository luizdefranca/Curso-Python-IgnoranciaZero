numconsumidores = 2
numprodutores = 4
nummensagens = 4

import threading, queue, time

Fila = queue.Queue()

def produtor(idnum):
    for msgnum in range(nummensagens):
        time.sleep(idnum)
        Fila.put('[produtor id=%d, cont=%d]' % (idnum, msgnum))

def consumidor(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = Fila.get(block=False)
        except queue.Empty:
            pass
        else:
            print('consumidor', idnum, 'recebeu =>', data)

if __name__ == '__main__':

    for i in range(numconsumidores):
        thread = threading.Thread(target=consumidor, args=(i,))
        thread.daemon = True
        thread.start()
        espera = []

    for i in range(numprodutores):
        thread = threading.Thread(target=produtor, args=(i,))
        espera.append(thread)
        thread.start()
    
    for thread in espera: thread.join()
    print('Sai da thread principal.')
