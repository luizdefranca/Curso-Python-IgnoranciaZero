import os

def filho():
    print('Ola do filho', os.getpid())
    os._exit(0)

def pai():
    while True:
        newpid = os.fork()
        if newpid == 0:
            filho()
        else:
            print('Ola do pai', os.getpid(), newpid)
        if input() == 'q':
            print("Fechando o pai", os.getpid())
            break

pai()
