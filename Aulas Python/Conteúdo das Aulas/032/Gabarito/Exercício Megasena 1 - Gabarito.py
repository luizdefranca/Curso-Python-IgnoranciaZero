"""
Reescreva o simulador da megasena de forma que agora em vez de trabalhar com
o mesmo jogo sempre, o programa seleciona aleatoriamento o jogo do teórico
jogador. Faça apenas um teste a não ser que você resolva deixar o pc ligado
o dia inteiro.
"""


import random

selecionado = [0]
sorteado = [1]

megasena = list(range(1,61))

cont = 0

while sorteado != selecionado:
    cont += 1

    sorteado = []
    selecionado = []

    mega_copy = megasena.copy()

    for i in range(6):
        ele_sele = random.choice(mega_copy)
        ele_sort = random.choice(mega_copy)

        selecionado.append(ele_sele)
        sorteado.append(ele_sort)

        mega_copy.remove(ele_sele)
        if ele_sele != ele_sort:
            mega_copy.remove(ele_sort)
            

    selecionado.sort()
    sorteado.sort()


print(cont)
    
        
