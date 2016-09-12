from array import array
from copy import copy

#Valores representando cada uma das peças no jogo
PRETO = -1
BRANCO = 1
VAZIO = 0

#Tamanho do jogo
TAMANHO_JOGO = 5

#Número total de soluções
TOTAL = 0

def RecebeEntrada():
    """
    Recebe uma entrada do usuário, e certifica
    que a entrada foi feita adequadamente
    """
    global TAMANHO_JOGO

    while True:

        #Primeiro nós pegamos uma entrada do usuário
        e = input("Digite o jogo inicial: \n")

        #Se a entrada não estiver separada adequadamente
        #a hora que dermos split na nossa string teremos
        #uma lista de tamanho diferente de 5, nesse caso
        #temos uma entrada inadequada
        lista = e.split()
        if len(lista) != TAMANHO_JOGO:
            print('Digite os valores das peças adequadamente espaçados')
            continue

        #Um segundo problema pode ocorrer se qualquer um
        #dos valores colocados for diferente de P ou B
        adequado = True
        for l in lista:
           u = l.upper()
           if u != 'P' and u != 'B':
               print('Digite apenas as letras P ou B')
               adequado = False
               break
        if not adequado:
            continue
        
        #Caso não haja nenhum problema na entrada do usuário
        #nós retornamos a lista
        return lista

def MontaJogo(lista):
    """
    Monta o jogo a partir da entrada do usuário
    (implementado usando array)
    """
    global PRETO, BRANCO

    #Criamos um array de signed shorts
    #para representar o nosso jogo
    jogo = array('h')

    #Percorremos cada uma das letras colocadas na lista
    for l in lista:
        #Convertemos ela para maiuscula
        u = l.upper()
        #Se a letra for P colocamos um -1 no array
        if u == 'P':
            jogo.append(PRETO)
        #Caso contrário temos uma peça branca
        else:
            jogo.append(BRANCO)

    #Por fim devolvemos nosso array
    return jogo

def FazJogada(jogo, i):
    """
    Função que realiza uma determinada jogada.
    Recebe o array do jogo e a posição i, onde
    é preciso fazer a jogada.
    """
    global TAMANHO_JOGO
    
    #Se for possível virar a peça a esquerda da
    #nossa posição
    if i-1 >= 0:
        jogo[i-1] *= -1
    #Se for possível virar a peça a direita da
    #nossa posição
    if i+1 < TAMANHO_JOGO:
        jogo[i+1] *= -1

    #E por fim nós removemos a peça
    jogo[i] = 0

def AcabouJogo(jogo):
    """
    Função que verifica se o jogo acabou
    """
    global VAZIO

    #Percorremos cada elemento no jogo
    for p in jogo:
        #Se a peça não tiver sido removida
        if p != VAZIO:
            #Nós informamos que o jogo não acabou
            return False
    #Caso todas as posições estejam vazias, o jogo acabou
    return True

def TodasJogadas(jogo):
    """
    Função que devolve todas as possíveis jogadas
    para uma determinada situação no tabuleiro
    """
    global TAMANHO_JOGO, PRETO
    
    #Criamos um array para todas as possíveis jogadas
    jogadas = array('h')

    #Olhamos cada uma das peças no jogo
    for i in range(TAMANHO_JOGO):
        #Se a peça for preta nós podemos fazer a jogada
        if jogo[i] == PRETO:
            #Então nós a adicionamos ao array de jogadas
            jogadas.append(i)
    
    #Por fim retornamos o array
    return jogadas

def ResolveJogo(jogo):
    """
    Obtem todas as possíveis maneiras de resolver
    o jogo
    """
    global TOTAL

    #primeiro nós criamos uma lista que conterá todos os jogos
    todos_jogos = [jogo]

    #Primeiro nós percorremos cada uma das possíveis jogadas
    jogadas = TodasJogadas(jogo)

    #inserimos um loop para percorrer todos os jogos
    #até que não exista mais nenhum
    while len(todos_jogos) > 0:
        #Inicializamos o valor de i
        i = 0

        #percorreremos cada jogo dentro do array
        while i < len(todos_jogos):
            #para cada jogo verificaremos o número de jogadas
            jogadas = TodasJogadas(todos_jogos[i])

            #O número k servirá para saber quantas posições foram
            #inseridas, assim o valor i poderá pular estas posições
            #adequadamente
            k = 0

            #percorremos cada uma das jogadas possíveis para
            #o array na posição i
            for j in jogadas:
                #fazemos uma cópia
                copia = copy(todos_jogos[i])

                #Realizamos a jogada
                FazJogada(copia, j)

                #Depois de fazer a jogada verificamos se o jogo acabou
                if AcabouJogo(copia):
                    #Se este for o caso, encontramos um ramo onde é
                    #possível ganhar o jogo, e nesse caso nós incrementamos
                    #o valor de total
                    TOTAL += 1

                #Caso contrário
                else:
                    #Adicionamos o jogo a lista contendo todos os jogos, pois
                    #deveremos jogar novamente
                    todos_jogos.insert(i+1, copia)
                    #E incrementamos k pois devemos pular esse array
                    k += 1

            #Removemos o array que nós acabamos de fazer
            todos_jogos.pop(i)
            
            #e incrementamos o valor de i
            i += k

def main():
    """
    Função principal do aplicativo
    """
    global TOTAL

    #Primeiro nós pegamos a entrada do usuário
    lista = RecebeEntrada()
    
    #A partir dela nós montamos o array do jogo
    jogo = MontaJogo(lista)

    #Então nós obtemos todas as possíveis soluções do jogo
    ResolveJogo(jogo)

    #E imprimimos esse valor
    print('Número de soluções possíveis:', TOTAL)

if __name__ == '__main__':
    main()
    
