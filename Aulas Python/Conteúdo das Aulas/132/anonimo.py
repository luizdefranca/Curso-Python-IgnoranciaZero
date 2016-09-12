import os, time, threading

def filho(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz+1) % 5

def pai(pipein):
    while True:
        linha = os.read(pipein, 32)
        print('Pai %d recebeu [%s] as %s' % (os.getpid(), linha, time.time()))

pipein, pipeout = os.pipe()
threading.Thread(target=filho, args=(pipeout,)).start()
pai(pipein)
