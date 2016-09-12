"""
São dados dois números inteiros positivos p e q,
sendo que o número de dígitos de p é menor ou igual ao número de dígitos de q.
Verificar se p é um subnúmero de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.

Reescreva o exercício usando funções, break e continue
"""
def main():
    """
    Função Principal do programa
    """
    p = int(input("Digite o valor de p: "))
    q = int(input("Digite o valor de q: "))

    #Calcula o numero de digitos de p
    cont_d = contaDigitos(p)

    #Comparação
    #p é sub de q --> paro execução
    #q == 0
    aux_q = q
    while True:
        subnum = aux_q%(10**cont_d)
        if subnum == p:
            break

        aux_q //= 10

        if aux_q == 0:
            break

    if subnum == p:
        print("%i é subnumero de %i" %(p, q))
    else:
        print("%i não é subnumero de %i" %(p, q))


def contaDigitos(num):
    """
    Recebe um numero inteiro e devolve o número
    de dígitos que esse número possuí
    """
    cont = 0
    while num!=0:
        num //=10
        cont+=1

    return cont

main()


