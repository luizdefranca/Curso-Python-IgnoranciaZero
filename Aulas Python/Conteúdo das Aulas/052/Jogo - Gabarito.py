"""
Jogo simples de ataque e cura
"""
#importa o modulo random
import random

def Salvar(player_vida, player_sp, inimigos):
    """
    Função usada para salvar o jogo
    """
    save = open('salvo.txt', 'w')

    save.write('Player\nVida = %i\nSP = %i\n'%(player_vida, player_sp))
    save.write("\n")
    save.write("Inimigos\n")
    for inimigo in inimigos:
        save.write(str(inimigo[0]) + ' ' + str(inimigo[1]) + '\n')

def CarregaJogo():
    """
    Função que carrega um jogo
    """
    load = open('salvo.txt', 'r')

    load.readline()

    player_vida = int(load.readline().split(' = ')[1])
    player_sp = int(load.readline().split(' = ')[1])

    load.readline()
    load.readline()

    inimigos = []
    linha = load.readline()

    while linha != '':
        inimigos.append([int(linha.split()[0]), int(linha.split()[1])])
        linha = load.readline()

    return player_vida, player_sp, inimigos

def main():
    """
    Função Principal do Jogo
    """
    print("BATALHA INJUSTA")

    #Preiro vemos se o usuário quer carregar ou iniciar um novo jogo
    opção = SelecionaOpção()

    #Chamamos a função apropriada de acordo com sua escolha
    if opção.startswith('n'):
        player_vida, player_sp, inimigos = NovoJogo()
    else:
        player_vida, player_sp, inimigos = CarregaJogo()

    #Enquanto essa variável for True estaremos rodando o jogo
    jogando = True 
    while jogando: #Nosso loop do jogo
        imprimeInfoPlayer(player_vida, player_sp)

        #pedimos para o player escolher o que fazer
        atk = oqueFazer()

        #se ele escolher atacar, devemos:
        if atk.startswith('a'):
            Atacar(inimigos)
            player_vida, player_sp, jogando = RealizaOperações(player_vida, player_sp, inimigos)

        #caso contrário ele escolheu curar
        elif atk.startswith('c'):
            #só podemos curar se o sp do player for maior do que 10
            if player_sp >= 10:
                player_vida, player_sp = Curar(player_vida, player_sp)
                
            #se o player tiver menos de 10 de sp
            else:
                #imprimimos que o player nao pode se curar
                print("Sp insuficiente!")

            player_vida, player_sp, jogando = RealizaOperações(player_vida, player_sp, inimigos)

        #se o player escolhar salvar
        elif atk.startswith('s'):
            Salvar(player_vida, player_sp, inimigos)

        #Se o player desistir
        else:
            #Nós dizemos que a variável jogando é falsa
            jogando = False

def SelecionaOpção():
    """
    Recebe uma entrada válida sobre o que o usuário quer
    fazer
    """
    while True:
        opção = input("Deseja carregar um jogo (c) ou iniciar um novo jogo(n)?\n").lower()

        if opção.startswith('n') or opção.startswith('c'):
            return opção
        else:
            print("Opção inválida, digite novamente.")

def NovoJogo():
    """
    Cria um novo jogo
    """

    #vida padrao de um inimigo
    inimigo_vida = 50

    inimigos = criaInimigos(inimigo_vida)

    return 500, 100, inimigos

def criaInimigos(inimigo_vida):
    """
    Função que criará uma lista de n inimigos
    selecionada pelo usuário
    """
    #determina o número de inimigos
    n = int(input("Digite o número de inimigos:\n"))

    #vetor que armazena todos os inimigos
    inimigos = []

    #adcionamos ao vetor um vetor com 2 componentes:
    #o número do inimigo e sua vida
    for i in range(n):
        inimigos.append([i+1,inimigo_vida])

    return inimigos

def imprimeInfoPlayer(HP, SP):
    """
    Imprime a vida e o sp do player na tela
    """
    #Imprimimos na tela a vida
    print("Vida:", HP)
    #e o sp do player
    print("SP:", SP)

def oqueFazer():
    """
    Função que garente que o usuário digitará uma opção
    válida
    """
    while True:
        escolha = input("Deseja atacar (a), curar (c), salvar(s), ou desistir(d)?\n").lower()

        if not escolha.isalpha():
            print("Digite apenas letras.")
        elif not (escolha.startswith('a') or escolha.startswith('c') or escolha.startswith('s') or escolha.startswith('d')):
            print("Digite uma opção válida")
        else:
            return escolha
            
def Atacar(inimigos):
    """
    Função realiza operações relacionadas a escolha do player
    em atacar
    """
    #escolher aleatoriamente um inimigo para ser atacado
    selecionado = random.choice(inimigos)

    #determinar o dano causado
    dano = random.randint(10, 15)

    #imprimir essas informações para o usuário
    print("Causou %i de dano ao inimigo %i!"%(dano, selecionado[0]))

    #diminuir da vida do inimigo o dano
    selecionado[1] -= dano

    #se a vida do inimigo for zerada, devemos:
    if selecionado[1] <= 0:
        #dizer que o inimigo morreu
        print("Inimigo %i morreu!"%selecionado[0])

        #e remover esse inimigo da lista de inimigos
        inimigos.remove(selecionado)

def Curar(player_vida, player_sp):
    """
    Função realiza operações relacionadas a escolha do player
    em curar
    """
    #escolhemos um valor aleatório para a cura
    cura = random.randint(10, 15)

    #imprimimos quanto o player recebeu de cura
    print("Você recebeu %i de vida!"%cura)

    #adcionamos isso a vida do player
    player_vida += cura

    #e diminuimos em 10 o sp do player
    player_sp -= 10

    return player_vida, player_sp

def RealizaOperações(player_vida, player_sp, inimigos):
    """
    Realiza os calculos e ataques depois do player ter
    escolhido uma ação
    """

    player_vida = AtaqueInimigo(player_vida, inimigos)

    #depois devemos aumentar o sp do player
    if player_sp < 100:
        #aumentamos em 3 toda rodada
        player_sp += 3
    #mas o player nunca pode ter mais de 100 de sp
    if player_sp > 100:
        player_sp = 100

    #depois verificamos se o jogo acabou
    jogando = VerificaSeAcabou(player_vida, inimigos)

    return player_vida, player_sp, jogando


def AtaqueInimigo(player_vida, inimigos):
    #depois disso é a vez dos inimigos atacarem
    for inimigo in inimigos:
        #escolhemos se o inimigo vai acertar ou errar
        #o inimigo tem 75% de chance de acertar
        acertou = bool(random.choice([1,1,1,0]))

        #se ele acertar, devemos:
        if acertou:
            #escolher um dano causado ao player
            dano = random.randint(1, 3)

            #imprimir a msg do dano
            print("Inimigo %i causou %i de dano!"%(inimigo[0], dano))

            #diminuir a vida do player
            player_vida -= dano

        #caso contrário
        else:
            #devemos informar que o inimigo errou
            print("Inimigo %i errou o ataque!"%inimigo[0])

    return player_vida

def VerificaSeAcabou(player_vida, inimigos):
    """
    Verifica se o jogo acabou, observando a vida do player
    e o número de inimigos
    """
    #se a vida do player for < 0 ele perdeu
    if player_vida <= 0:
        print("Perdeu o jogo!")
        return False
    #se o número de inimigos for zero ele venceu
    if len(inimigos) == 0:
        print("Parabens você ganhou o jogo!")
        return False

    return True

main()

