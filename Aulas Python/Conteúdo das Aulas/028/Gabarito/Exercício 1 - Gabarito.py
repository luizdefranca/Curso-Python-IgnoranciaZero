"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus
telespectadores para saber qual o melhor jogador após cada jogo.
Para isto, faz-se necessário o desenvolvimento de um programa, que será
utilizado pelas telefonistas, para a computação dos votos.

Sua equipe foi contratada para desenvolver este programa, utilizando a
linguagem de programação Python.
Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador.
Um número de jogador igual zero, indica que a votação foi encerrada.
Se um número inválido for digitado, o programa deve ignorá-lo,
voltando a pedir outro número.
Após o final da votação, o programa deverá exibir:

a.	O total de votos computados;
b.	Os númeos e respectivos votos de todos os jogadores que receberam votos;
c.	O percentual de votos de cada um destes jogadores;
d.	O número do jogador escolhido como o melhor jogador da partida,
        juntamente com o número de votos e o percentual de votos dados a ele.

Observe que os votos inválidos e o zero final não devem ser computados como
votos. O resultado aparece ordenado pelo número do jogador.
O programa deve fazer uso de listas.

Exemplo de execução:
>>> 
Enquete: Quem foi o melhor jogador?

Informe um valor entre 1 e 23 ou 0 para sair!

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da Votação: 

Foram computados 8 votos

Jogador          Votos          %
   9                4          50.0%
  10                3          37.5%
  11                1          12.5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50.0% do total de votos.
>>> 
"""

print("Enquete: Quem foi o melhor jogador?\n")

print("Informe um valor entre 1 e 23 ou 0 para sair!\n")

votos = []
voto = int(input("Número do jogador (0=fim): "))

while voto != 0:
    if 1 <= voto <= 23:
        votos.append(voto)
    voto = int(input("Número do jogador (0=fim): "))

print("\nResultado da Votação: \n")

print("Foram computados %i votos\n"%len(votos))

print("Jogador          Votos          %")

melhor = 1
maior_n_votos = 0
porcentagem = 0
for i in range(1, 24):
    total_de_votos_em_i = votos.count(i)
    porcentagem_de_votos_em_i = 100*total_de_votos_em_i/len(votos)
    if total_de_votos_em_i > 0:
        print("%4.i             %4.i          %.1f%%"%(i, total_de_votos_em_i, porcentagem_de_votos_em_i))

        if total_de_votos_em_i > maior_n_votos:
            maior_n_votos = total_de_votos_em_i
            melhor = i
            porcentagem = porcentagem_de_votos_em_i

print("O melhor jogador foi o número %i, com %i votos, correspondendo a %.1f%% do total de votos."%(melhor, maior_n_votos, porcentagem))
