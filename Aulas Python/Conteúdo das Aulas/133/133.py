import os

print("Modulo multiprocessing")

input()

print("Permite realizar processos tem")
print("paralelo criando efetivamente um")
print("processo diferente de threads.")

input()

print("Vantagens: ")
print("Funciona em várias plataformas distintas")
print("diferente do os.fork")
print("Perde em velocidade para threads porém")
print("efetivamente executa os programas em núclos")
print("distintos da CPU")

input()

print("Desvantagens: ")
print("Mudanças em um processo não afetam o")
print("outro")
print("Algumas estruturas (como o lambda) não")
print("podem ser rodadas em paralelo")

input()

print("Aqui veremos uma breve introdução ao modulo")
print("e veremos que ele possui estruras semelhantes")
print("aos modulos threading e queue previamente")
print("estudados")

input()

print("Veja um primeiro exemplo simples.")

input()

os.system("python3 mult.py")

input()

print("""
No unix, usa um fork para criar um processo filho
e invoca o metodo run de Process para roda-lo

No windows um novo interpretador é criado usando
o processo de criação de ferramentas do Windows
passando um objeto codificado pelo pickle
para um novo processo por meio de um pipe e começando
o 'python -c' para rodar o programa o que o roda
com uma função especial construida em python que
le e decodifica o objeto e invoca o método run 
""")

input()

print("Vendo o funcionamento do programa no windows")
print("vemos que os objetos passado pelo process")
print("possuem a limitação de serem objetos que")
print("podem ser codificados pelo pickle")

input()

print("Além da comunicação interprocessual por")
print("meio de pipes nomeados o modulo")
print("multiprocessing possui algumas ferramentas")
print("que podem ser usadas para realizar a comunicação")
print("interprocessual")

input()

print("Multiprocess pipe")

input()

os.system('python3 pipe.py')

input()

print("Além de pipes podemos támbem usar queues")

input()

os.system('python queue.py')

input()

print("Multiprocessing também possui uma estrutura")
print("chamada event que permite que haja comunicação")
print("dos estados entre processos. O evento pode ter")
print("os estados 'set' e 'unset'")

input()

os.system('python3 event.py')

input()

print("Por fim nós temos as pools que permitem")
print("que um numero fixo de 'workers' possam")
print("ser usados em casos simples. Isso significa")
print("que dada um número de operações a serem")
print("realizadas e um número de recursos onde elas")
print("podem ser realizadas as pools vão alocar")
print("as operações nos recursos dada a limitação")
print("no número de recursos até que todas as")
print("operações sejam terminadas")

input()

os.system('python pool.py')

input()

print("E muitas outras coisas podem ser feitas")
print("utilizando o modulo multiprocessing")
print("cheque a documentação oficial do python")
print("e verá que as funcionalidades são muitas!")

input()
