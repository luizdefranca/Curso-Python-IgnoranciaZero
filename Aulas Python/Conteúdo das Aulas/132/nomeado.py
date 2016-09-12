import os, time, sys

fifonome = os.path.join(os.getcwd(), 'tmp', 'pipefifo')

def filho():
    pipeout = os.open(fifonome, os.O_WRONLY)
    zzz = 0
    while True:
        time.sleep(zzz)
        msg = ('Spam %03d\n' % zzz).encode()
        os.write(pipeout, msg)
        zzz = (zzz+1) % 5

def pai():
    pipein = open(fifonome)
    while True:
        linha = pipein.readline()
        print('Pai %d recebeu "%s" as %s' % (os.getpid(), linha, time.time()))

if __name__ == '__main__':
    if not os.path.exists(fifonome):
        os.mkfifo(fifonome)
    if len(sys.argv) == 1:
        pai()
    else:
        filho()
