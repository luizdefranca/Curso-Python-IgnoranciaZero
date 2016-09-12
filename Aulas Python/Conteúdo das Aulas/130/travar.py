import _thread as thread, time
def contador(meuId, cont):
    for i in range(cont):
        time.sleep(1)
        mutex.acquire()
        print('[%s] => %s' % (meuId, i))
        mutex.release()

mutex = thread.allocate_lock()
for i in range(5):
    thread.start_new_thread(contador, (i, 5))

time.sleep(6)
print('Saindo da thread principal.')
