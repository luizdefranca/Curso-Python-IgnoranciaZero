"""
44.	Em uma eleição presidencial existem quatro candidatos. Os votos são
informados por meio de código. Os códigos utilizados são:

o	1 , 2, 3, 4  - Votos para os respectivos candidatos 
o	(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
o	5 - Voto Nulo
o	6 - Voto em Branco

Faça um programa que calcule e mostre:
o	O total de votos para cada candidato;
o	O total de votos nulos;
o	O total de votos em branco;
o	A percentagem de votos nulos sobre o total de votos;
o	A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.
"""


print("1 - Jose\n2 - João\n3 - Pedro\n4 - Joana")
jose = joao = pedro = joana = nulo = branco = 0
voto = int(input("Digite seu voto: "))

while voto != 0:
    if voto == 1:
        jose += 1
    elif voto == 2:
        joao += 1
    elif voto == 3:
        pedro += 1
    elif voto == 4:
        joana += 1
    elif voto == 5:
        nulo += 1
    else:
        branco += 1

    voto = int(input("Digite seu voto: "))

print("Total de Votos: ")
print("Jose:", jose)
print("João:", joao)
print("Pedro:", pedro)
print("Joana:", joana)
print("Nulo:", nulo)
print("Branco:", branco)
total = jose+joao+pedro+joana+nulo+branco
print("Porcentagem de Votos nulos: %g%%"%(100*nulo/total))
print("Porcentagem de Votos brancos: %g%%"%(100*branco/total))
