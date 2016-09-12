import multiprocessing
import time

def espera_por_evento(e):
    """Espera a ocorrencia do evento antes de fazer qualquer coisa"""
    print('espera_por_evento: Iniciando')
    e.wait()
    print('espera_por_evento: e.is_set()->', e.is_set())

def espera_por_evento_timeout(e, t):
    """Espera t segundos para e depois timeout"""
    print('espera_por_evento_timeout: Iniciando')
    e.wait(t)
    print('espera_por_evento_timeout: e.is_set()->', e.is_set())


if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name='bloco', 
                                 target=espera_por_evento,
                                 args=(e,))
    w1.start()

    w2 = multiprocessing.Process(name='não-bloco', 
                                 target=espera_por_evento_timeout, 
                                 args=(e, 2))
    w2.start()

    print('main: esperando antes de chamar Event.set()')
    time.sleep(3)
    e.set()
    print('main: evento está pronto')
