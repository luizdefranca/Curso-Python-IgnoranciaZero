numconsumidores = 2
numprodutores = 4
nummensagens = 4

import _thread as thread, queue, time

print_seguro = thread.allocate_lock()

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
            with print_seguro:
                print('consumidor', idnum, 'recebeu =>', data)

if __name__ == '__main__':
    for i in range(numconsumidores):
        thread.start_new_thread(consumidor, (i,))
    for i in range(numprodutores):
        thread.start_new_thread(produtor, (i,))
        time.sleep(((numprodutores-1) * nummensagens) + 1)

    print('Sai da thread principal.')
