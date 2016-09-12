"""
Você já deve ter notado que é muito comum numa família, 
ou numa classe de escola haver pessoas que fazem aniversário
num mesmo dia. Se parar para pensar, como pode num grupo
de 50 pessoas haver duas pessoas, que dentre os 365 dias do ano,
fazem aniversário no mesmo dia? Esse fato é explicado por
estatística simples, mas vamos criar um programa para testa-lo.

Escreva um programa que recebe um número n de pessoas e um número
x de repetições e sorteia listas com datas de aniversário, e 
verifica se existe alguma data coincidente. Para cada loop
deve-se re-sortear as listas, e para cada lista onde há casos
coincidentes deve-se acrescentar 1 ao número de casos favoráveis.
Depois de rodados os x loops de a porcentegem de vezes em que
houveram aniversários coincidentes.

Detalhe: Use compressão de listas para gerar
as datas de aniversário
"""
import random

def main():
	while True:
		try:
			n = int(input('Digite o número de pessoas\n'))
			x = int(input('Digite o número de repetições\n'))
			assert n > 0
			assert x > 0
		except:
			print('erro na leitura de dados, digite novamente')
		else:
			break
	favoraveis = 0
	
	for i in range(x):
		l = geraListas(n)
		if checaCoincidente(l):
			favoraveis += 1
		
		#só para nos dar um feedback
		if i%10000 == 0:
			print('Já foram %i loops!'%i)

	p = 100*favoraveis/x

	print('A porcentagem favoravel foi de %.5f%%'%p)
		
		
def geraListas(n):
	return [random.randint(1,366) for i in range(n)]

def checaCoincidente(l):
	#só pra abusar de compressão,
	#mas totalmente desnecessário
	j = [True for i in l if l.count(i) > 1]
	if len(j) > 0:
		return True
	else:
		return False

main()


