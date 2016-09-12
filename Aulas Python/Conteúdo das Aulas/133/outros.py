import os
from multiprocessing import Process

def rodaprograma(arg):
    os.execlp('python', 'python3', 'filho.py', str(arg))

if __name__ == '__main__':
    for i in range(5):
        Process(target=rodaprograma, args=(i,)).start()
    print('Saiu de pai')
