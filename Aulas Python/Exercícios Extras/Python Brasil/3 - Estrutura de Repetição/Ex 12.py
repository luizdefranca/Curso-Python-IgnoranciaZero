"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
tabuada. A saída deve ser conforme o exemplo abaixo:
o	Tabuada de 5:
o	5 X 1 = 5
o	5 X 2 = 10
o	...
o	5 X 10 = 50
"""
num = int(input("Digite o numero a ser visto: "))

cont = 1
while cont <= 10:
    print("%i X %i = %i"%(num, cont, cont*num))
    cont += 1
