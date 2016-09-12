"""
Você foi contratado pela USP para criar
um programa que calcula os gastos da folha
de pagamento da universidade.

Para isso você recebeu um arquivo txt contendo
o gasto de cada um dos diversos funcionários da
universidade

O seu programa deve:
1) Pedir um valor percentual para calcular o aumento
2) Gerar uma lista com todos os valores 
3) Gerar uma lista com todos os valores corrigidos 
4) Escrever todos os valores corrigidos em um arquivo gastos_corrigidos.txt
5) Guardar as duas listas geradas num arquivo listas.obj 

Para resolver o exercício procure utilizar a função map
"""
import pickle

def main():
	#1 - Pegando a correção percentual
	p_cor = float(input('Digite o percentual de correção: '))
	v_cor = p_cor/100
	fator_cor = v_cor + 1
	
	#2 e 3 - Gerar as listas
	gastos = list(map((lambda x: float(x)), open('gastos.txt')))
	gastos_corrigidos = list(map((lambda x: x*fator_cor), gastos))
	
	#4 Escrever num arquivo txt
	with open('gastos_corrigidos.txt', 'w') as arq:
		for g in gastos_corrigidos:
			arq.write('%.2f'%g+'\n')

	#5 guardar as listas
	with open('listas.obj', 'wb') as arq:
		pickle.dump(gastos, arq)
		pickle.dump(gastos_corrigidos, arq)
main()	

	
