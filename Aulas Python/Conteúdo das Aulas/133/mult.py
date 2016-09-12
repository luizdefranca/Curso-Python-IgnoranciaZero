import os
from multiprocessing import Process, Lock

def quem_sou_eu(label, lock):
    msg = '%s: nome:%s, pid:%s'
    with lock:
        print(msg % (label, __name__, os.getpid()))

if __name__ == '__main__':
    lock = Lock()
    quem_sou_eu('chamada da função', lock)
    p = Process(target=quem_sou_eu, args=('filho criado', lock))
    p.start()
    p.join()
    for i in range(5):
        Process(target=quem_sou_eu, args=(('processo rodando %s' % i), lock)).start()
    with lock:
        print('Saida da main thread.')
