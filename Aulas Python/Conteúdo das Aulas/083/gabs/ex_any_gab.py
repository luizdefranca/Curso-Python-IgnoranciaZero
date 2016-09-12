"""
Um jogador lança um dado n vezes. Qual é a probabilidade pelo menos 1 numero menor do
que 3

Use um programa para decifrar este enigma
Lembre-se que a probabilidade são os casos possiveis por favoraveis
"""

#menino = False
#menina = True

#Com certeza não é o melhor algoritmo
#para fazer isso, mas eu estou com
#preguiça de pensar
import random
def combinaçõesPossiveis(ele, n):
	comb = []
	while len(comb) < len(ele)**n:
		n_comb = []
		for i in range(n):
			n_comb.append(random.choice(ele))
		if n_comb not in comb:
			comb.append(n_comb)
	return comb

n = int(input('Digite o número n de lançamentos: '))

comb = combinaçõesPossiveis(list(range(1,7)), n)

favoraveis = len([1 for c in comb if any([num < 3 for num in c])])
possiveis = len(comb)

print('A probabilidade é de %i/%i'%(favoraveis, possiveis))
