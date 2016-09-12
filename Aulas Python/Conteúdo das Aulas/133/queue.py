import multiprocessing
import time

class Consumidor(multiprocessing.Process):
    def __init__(self, tarefa_queue, resultado_queue):
        multiprocessing.Process.__init__(self)
        self.tarefa_queue = tarefa_queue
        self.resultado_queue = resultado_queue

    def run(self):
        proc_nome = self.name
        while True:
            prox_tarefa = self.tarefa_queue.get()
            if prox_tarefa is None:
                print('%s: Saindo' % proc_nome)
                self.tarefa_queue.task_done()
                break
            print('%s: %s' % (proc_nome, prox_tarefa))
            resposta = prox_tarefa()
            self.tarefa_queue.task_done()
            self.resultado_queue.put(resposta)
        return


class Tarefa(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        time.sleep(0.1)
        return '%s * %s = %s' % (self.a, self.b, self.a * self.b)
    def __str__(self):
        return '%s * %s' % (self.a, self.b)


if __name__ == '__main__':
    tarefas = multiprocessing.JoinableQueue()
    resultados = multiprocessing.Queue()
    
    num_consumidores = multiprocessing.cpu_count() * 2
    print('Criando %d consumidores' % num_consumidores)
    consumidores = [ Consumidor(tarefas, resultados)
                  for i in range(num_consumidores) ]
    for c in consumidores:
        c.start()
    
    num_trabalhos = 10
    for i in range(num_trabalhos):
        tarefas.put(Tarefa(i, i))
    
    for i in range(num_consumidores):
        tarefas.put(None)

    tarefas.join()
    
    while num_trabalhos:
        resultado = resultados.get()
        print('Resultado:', resultado)
        num_trabalhos -= 1
