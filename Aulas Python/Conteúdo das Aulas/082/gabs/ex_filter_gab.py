"""
Utilizando o que foi feito no programa
para a função map, a USP quer que você crie um
novo programa:

Nele você pegará todos os valores corrigidos
e os valores anteriores a correção a partir dos
objetos guardados em listas.obj e deverá:

1) Pedir um valor limite de correção
2) Criar uma lista com o valor monetário da correção
3) Filtrar os valores cuja correção não ultrapassa esse valor
4) Calcular a soma de todos os valores filtrados
5) Disponibilizar para o usuário o total de correção
"""
import pickle

def main():
	lmt = float(input('Digite o valor limite de correção: '))
	
	with open('listas.obj', 'rb') as arq:
		gastos = pickle.load(arq)
		gastos_corr = pickle.load(arq)

	corr = list(map((lambda x: gastos_corr[x] - gastos[x]), range(len(gastos))))
	
	filtrado = filter((lambda x: x <= lmt), corr)

	soma = 0
	for v in filtrado:
		soma += v

	print('A correção será de no total R$ %.2f'%soma)

main() 
