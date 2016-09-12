"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
"""

n = int(input("Digite o numero de eleitores: "))

candidato1 = candidato2 = candidato3 = 0

for cont in range (1, n+1):
    voto = int(input("Digite o voto do eleitor %i: "%cont))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    else:
        candidato3 += 1

    #cont += 1

if candidato1 > candidato2:
    if candidato1 > candidato3:
        print("Ganhou o primeiro candidato com %i votos" %candidato1)

elif candidato2 > candidato1:
    if candidato2 > candidato3:
        print("Ganhou o segundo candidato com %i votos" %candidato2)

elif candidato3 > candidato1:
    if candidato3 > candidato1:
        print("Ganhou o terceiro candidato com %i votos" %candidato3)
