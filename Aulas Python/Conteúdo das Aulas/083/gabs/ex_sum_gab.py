"""
Refaça o exercício ex_filter.py da aula 082
utilizando a função sum
"""

import pickle

def main():
	lmt = float(input('Digite o valor limite de correção: '))
	
	with open('listas.obj', 'rb') as arq:
		gastos = pickle.load(arq)
		gastos_corr = pickle.load(arq)

	corr = list(map((lambda x: gastos_corr[x] - gastos[x]), range(len(gastos))))
	
	filtrado = filter((lambda x: x <= lmt), corr)

	soma = sum(filtrado)

	print('A correção será de no total R$ %.2f'%soma)

main() 
