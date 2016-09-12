import os

parm = 0

while True:
    parm += 1
    # copia processo
    pid = os.fork()
    if pid == 0:
        os.execlp('python3', 'python3', 'filho.py', str(parm))
        assert False, 'error starting program'
    else:
        print('Filho é', pid)
        if input() == 'q': break
