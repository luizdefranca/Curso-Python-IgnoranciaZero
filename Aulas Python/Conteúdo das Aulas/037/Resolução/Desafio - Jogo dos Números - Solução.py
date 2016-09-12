"""
Escreva o jogo dos números como descrito na aula. Utilize as funções escritas
em aula e mais três feitas agora:
    1 - VerificaSeVenceu: Recebe uma matriz 4x4 e verifica se os números estão
    ordenados de forma que o jogador venceu
    2 - VerificaJogada: Verifica se a jogada escolhida pelo usuário é válida
    3 - ImprimeJogo: Função que imprime o jogo na tela do usuário
Você pode fazer quantas funções adcionais quanto quiser

Organize o seu jogo dentro da função main. Dê para o usuário a toda rodada
a opção de desistir(0) ou de inserir uma posição(1), a posição inserida
será feita colocando a linha e coluna da matriz, por exemplo 11 significa que
estamos nos referenciando ao elemento da linha 1 coluna 1, 32 se referencia ao
elemento da linha 3 coluna 2
"""

import random

#############################################################
#   Funções Feitas em Aula                                  #
#############################################################

def TrocaElemento(pos1, pos2, matriz):
    elemento1 = matriz[pos1//10 -1][pos1%10 -1]
    elemento2 = matriz[pos2//10 -1][pos2%10-1]
    matriz[pos1//10-1][pos1%10-1] = elemento2
    matriz[pos2//10-1][pos2%10-1] = elemento1


def geraMatriz(matriz):
    lista = list(range(16))
    for j in range(4):
        linha = []
        for i in range(4):
            x = random.choice(lista)
            linha.append(x)
            lista.remove(x)
        matriz.append(linha)

#############################################################
#   Funções Propostas                                       #
#############################################################

def VerificaSeVenceu(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if ((4*i + j + 1) != matriz[i][j] and i != 3 and j != 3) or (i == 3 and j == 3 and matriz[i][j] != 0):
                return False

    return True

def VerificaJogada(pos, zero_pos):
    linha = pos//10
    coluna = pos%10

    linha_zero = zero_pos//10
    coluna_zero = zero_pos%10

    if linha < 1 or linha > 4 or coluna < 1 or coluna > 4:
        return False
    else:
        if (linha == linha_zero -1 and coluna == coluna_zero) or (linha == linha_zero and (coluna == coluna_zero-1 or coluna == coluna_zero+1)) or (linha == linha_zero+1 and coluna == coluna_zero):
            return True
        else:
            return False


def imprimeJogo(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

#############################################################
#   Funções Pessoais                                        #
#############################################################

def AchaPosZero(matriz):
    #Função que procura e devolve a posição do zero da matriz(espaço vazio)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 0:
                return (i+1)*10 + j+1

def fazJogada(jogo):
    #Imprime o jogo na tela e pergunta se o usuário quer continuar
    imprimeJogo(jogo)
    dec = bool(int(input("Deseja continuar(1) ou desistir(0): ")))
    return dec

#############################################################
#   Função Main                                             #
#############################################################

def main():
    jogo = []
    geraMatriz(jogo)

    venceu =False

    zero_pos = AchaPosZero(jogo)

    jogando = fazJogada(jogo)


    while jogando:
        pos = int(input("Digite a posição do elemento que você deseja trocar: "))

        while not VerificaJogada(pos, zero_pos):
            print("Entrada inválida. Digite novamente")
            pos = int(input("Digite a posição do elemento que você deseja trocar: "))

        TrocaElemento(pos, zero_pos, jogo)

        zero_pos = pos

        venceu = VerificaSeVenceu(jogo)
        jogando = not venceu

        if jogando:
            jogando = fazJogada(jogo)

    if venceu:
        print("Parabens, você venceu!!!")
    else:
        print("Obrigado por jogar.")

main()
