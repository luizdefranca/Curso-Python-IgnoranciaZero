"""
São dados dois números inteiros positivos p e q,
sendo que o número de dígitos de p é menor ou igual ao número de dígitos de q.
Verificar se p é um subnúmero de q.

Exemplos:
p = 23, q = 57238, p é subnúmero de q.
p = 23, q = 258347, p não é subnúmero de q.
"""
p = int(input("Digite o valor de p: "))
q = int(input("Digite o valor de q: "))

#Calcula o numero de digitos de p
aux_p = p
cont_d = 0
while aux_p != 0:
    aux_p //=10
    cont_d+=1


#Comparação
#p é sub de q --> paro execução
#q == 0
comparando = True
aux_q = q
while comparando:
    subnum = aux_q%(10**cont_d)
    if subnum == p:
        comparando = False

    aux_q //= 10

    if aux_q == 0:
        comparando = False

if subnum == p:
    print("%i é subnumero de %i" %(p, q))
else:
    print("%i não é subnumero de %i" %(p, q))
    

