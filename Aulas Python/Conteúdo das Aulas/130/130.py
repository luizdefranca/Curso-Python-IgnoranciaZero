import os, sys

if 'win' in sys.platform:
    p = 'python'
else:
    p = 'python3'

print("Threads: Modulo _thread")

input()

print("Threads são como forks entretanto são")
print("usados para executar objetos em um mesmo")
print("processo, o que lhes garante uma melhor")
print("performance, simplicidade, compartilhamento")
print("de memória e portabilidade")

input()

print("Um dos problemas mais notáveis de threads")
print("é para sincronizar operações, uma vez que")
print("mesmo operações simples como printar texto")
print("na tela pode gerar conflitos. Veremos a frente")
print("que por debaixo dos panos de fato apenas")
print("uma thread está sendo realmente executada")
print("pelo interpretador de python")

os.system(p + ' hello_thread.py')

input()

print("Note que como as funções retornam um valor")
print("imediato temos que cada função é executada")
print("em uma thread a cada loop da função pai")
print("Entretanto o verdadeiro poder das threads")
print("é mostrado abaixo:")

os.system(p + ' poder.py')

input()

print("Note que temos a execução paralela da função")
print("no programa, entretanto um cuidado que devemos")
print("ter é ao compartilhar objetos, pois se duas threads")
print("tentarem modificar o objeto ao mesmo tempo isso")
print("poderá causar erros terríveis.")

input()

print("Para compartilhar objetos o melhor")
print("é travar cada um deles, veja o próximo")
print("exemplo.")

os.system(p + ' travar.py')

input()

print("Veja que o objeto mutex serve para travar")
print("a execução de uma thread, isso permite")
print("um acesso organizado a determinado recursos")
print("do programa de maneira simples")

input()

print("Além disso podemos utilizar as travas")
print("para organizar a realização de determidas")
print("operações, evitar colisões e realizer a")
print("comunicação entre determinadas operações tais")
print("como mapear a saída execução de uma dada função")
print("Por exemplo: ")

os.system(p + ' travar_sair.py')

input()

print("Threads: Modulo threading")

input()

print("O módulo _thread realiza operações de")
print("baixo nível enquanto que o módulo threading")
print("implementa objetos baseados no módulo _thread")

os.system(p + ' hello_threading.py')

input()
