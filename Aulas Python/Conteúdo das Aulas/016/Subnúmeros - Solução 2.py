"""
São dados dois números inteiros positivos p e q,
sendo que o número de dígitos de p é menor ou igual ao número de dígitos de q.
Verificar se p é um subnúmero de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.
"""
#p = 23
#q = 572   3  8

#-------------------
#dig = p%10 ==> 3
#dig2 = q%10 ==> 8
# 3 == 8 --> q//10 = 5723
#---------------
#dig = p%10 ==> 3
#dig2 = q%10 ==> 3
# 3 == 3 --> q//10 = 573  p//10 =2
# dig = p%10 ==> 3
# dig2 = q%10 ==> 2
# 2 == 2 --> q//10 = 57 p//10 = 0

p = int(input("Digite o valor de p: "))
q = int(input("Digite o valor de q: "))

aux_p = p
aux_qM = q
rodando = True
#se aux_p == 0 --> rodando = False
#se aux_qM ==0 --> rodando = False
while rodando:
    aux_qm = aux_qM
    continuar = True
    while continuar:
        if aux_p%10 == aux_qm%10:
            aux_p //=10
            aux_qm //=10
        else:
            aux_p = p
            continuar = False

        if aux_p == 0:
            continuar = rodando = False

    aux_qM //= 10

    if aux_qM == 0:
        rodando = False

if aux_p == 0:
    print("%i é subnúmero de %i"%(p,q))
else:
    print("%i não é subnúmero de %i"%(p,q))
