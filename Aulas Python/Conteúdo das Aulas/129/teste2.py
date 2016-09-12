import os, time

def contador(cont):
    for i in range(cont):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))

for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Processo %d criado' % pid)
    else:
        contador(5)
        os._exit(0)

print('Processo principal acabado.')
