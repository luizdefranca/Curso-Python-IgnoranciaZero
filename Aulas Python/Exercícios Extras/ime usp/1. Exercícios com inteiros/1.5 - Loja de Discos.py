"""
Uma loja de discos anota diariamente durante o mês de março
a quantidade de discos vendidos. Determinar em que dia desse mês
ocorreu a maior venda e qual foi a quantidade de discos vendida nesse dia.
"""

cont = 0
n = 29
dia = int(input("Digite o dia da venda: "))
soma = int(input("Digite a venda do dia: "))
segundo = int(input("Digite o dia da venda: "))
somas = int(input("Digite a venda do dia: "))

while cont < n:
    if soma > somas:
        segundo = int(input("Digite o dia da venda: "))
        somas = int(input("Digite a venda do dia: "))
    else:
        dia = int(input("Digite o dia da venda: "))
        soma = int(input("Digite a venda do dia: "))
    cont = cont + 1
if soma > somas:
    print ("No dia", dia, " houve a maior venda de discos, que foi igual a",soma)
if somas > soma:
    print ("No dia", segundo, " houve a maior venda de discos, que foi igual a",somas)
