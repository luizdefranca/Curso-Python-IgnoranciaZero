import os
from multiprocessing import Process, Pipe

def sender(pipe):
    """
    Manda o objeto para pai por meio de um pipe anônimo
    """
    pipe.send(['spam'] + [42, 'ovos'])
    pipe.close()

def comunicador(pipe):
    """
    Manda e recebe objetos por um pipe
    """
    pipe.send(dict(nome='João', spam=42))
    resposta = pipe.recv()
    print('comunicador recebeu:', resposta)

if __name__ == '__main__':
    (saidaPai, saidaFilho) = Pipe()
    Process(target=sender, args=(saidaFilho,)).start()
    print('pai recebeu:', saidaPai.recv())
    saidaPai.close()
    
    (saidaPai, saidaFilho) = Pipe()
    filho = Process(target=comunicador, args=(saidaFilho,))
    filho.start()
    print('pai recebeu:', saidaPai.recv())
    saidaPai.send({x * 2 for x in 'spam'})
    filho.join()

    print('saiu de pai')
