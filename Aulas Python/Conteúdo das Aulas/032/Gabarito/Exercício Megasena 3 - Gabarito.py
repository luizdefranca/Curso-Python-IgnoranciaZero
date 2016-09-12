"""
Modifique o exercício 2 para que agora seja contabilizado os ganhos do jogador.
Para isso agora o programa não para quando o usuário ganha, ele roda um total
de 50.063.860 loops. O valor acumulado da megasena varia entre 1.5 milhoes
e 70 milhões (em média), sendo que a quina corresponde entre 0.1 e 0.4% do valor
do prêmio, e a quadra entre 1/30000 e 1/5000 do valor total do prêmio, e
o grande vencedor leva 94% do acumulado. O gasto de cada bilhete é R$ 2.5
"""
import random

megasena = list(range(1,61))
meu = [6, 13, 25, 33, 42, 50]

ganho = 0

for i in range(50063860):
    acumulado = random.uniform(1.5, 70)*1000000

    sorteado = []

    mega_copy = megasena.copy()

    for j in range(6):
        ele_sort = random.choice(mega_copy)
        sorteado.append(ele_sort)
        mega_copy.remove(ele_sort)

    sorteado.sort()

    iguais = 0

    for k in range(len(sorteado)):
        if sorteado[k] == meu[k]:
            iguais += 1

    if iguais == 4:
        quadra = random.uniform(1/30000, 1/5000)*acumulado
        ganho += quadra
    elif iguais == 5:
        quina = random.uniform(0.001, 0.004)*acumulado
        ganho += quina
    elif iguais == 6:
        ganho += acumulado*0.94

    ganho -= 2.5

print("No final o usuário saiu com saldo R$%.2f"%ganho)
