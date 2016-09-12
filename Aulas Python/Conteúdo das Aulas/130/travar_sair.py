import _thread as thread

stdoutmutex = thread.allocate_lock()
exitmutexes = [False] * 10

def contador(meuId, cont):
    for i in range(cont):
        stdoutmutex.acquire()
        print('[%s] => %s' % (meuId, i))
        stdoutmutex.release()
    exitmutexes[meuId] = True

for i in range(10):
    thread.start_new_thread(contador, (i, 100))

while False in exitmutexes: pass

print('Saindo da thread principal.')
