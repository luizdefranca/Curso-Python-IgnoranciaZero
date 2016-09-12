"""
38.	Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:
 .	Esse funcionário foi contratado em 1995, com salário inicial de
 R$ 1.000,00;

a.	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
b.	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem
ao dobro do percentual do ano anterior.

Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o
salário inicial do funcionário.

"""

salário_inicial = float(input("Digite o salário inicial: "))

salário = salário_inicial * 1.015
aumento = 1.5

for i in range(2014-1997):
    aumento *= 2
    salário *= (1+ aumento/100)
    print(salário)

print("Salário Atual: R$",salário)
