import random

def VerificaEntrada(num):
    """
    Retorna um booleano dizendo se a entrada é válida
    ou não, tendo em vista o número de dígitos
    True --> Entrada Válida
    False --> Entrada Inválida
    """
    if num < 1000 or num >= 10000:
        return False
    else:
        return True

def GeraSecretNum():
    """
    Função que gera e retorna o número secreto
    E a lista contendo cada um de seus dígitos
    Exemplo
    secretNum = 1783
    list_num = [1,7,8,3]
    """
    numeros = list(range(10))
    secretNum = 0

    while numeros[0] == 0:
        random.shuffle(numeros)
    
    for i in range(4):
        dig = numeros[i]
        secretNum += dig*(10**(3-i))

    return secretNum, numeros[:4]
                

def GeraDicas(num, secretNum, secretNumList):
    """
    Recebe o número escolhido e o número secreto
    e gera uma lista contendo as dicas a serem
    colocadas.
    Código
    --> 0 = Bagels
    --> 1 = Pico
    --> 2 = Fermi

    Retorna uma lista vazia caso os dois números sejam iguais
    """

    if num == secretNum:
        return []

    dica = []

    for i in range(4):
        dig = num % 10
        if dig == secretNumList[3-i]:
            dica.append(2) #Fermi
        elif dig in secretNumList:
            dica.append(1) #Pico
        num //= 10

    if len(dica) == 0:
        dica.append(0) #Bagels

    dica.sort()

    return dica

        
