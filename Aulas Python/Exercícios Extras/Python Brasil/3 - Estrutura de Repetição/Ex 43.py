"""
43.	O cardápio de uma lanchonete é o seguinte:
o	Especificação   Código  Preço
o	Cachorro Quente 100     R$ 1,20
o	Bauru Simples   101     R$ 1,30
o	Bauru com ovo   102     R$ 1,50
o	Hambúrguer      103     R$ 1,20
o	Cheeseburguer   104     R$ 1,30
o	Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total
geral do pedido. Considere que o cliente deve informar quando o pedido deve
ser encerrado.

"""

encerra = False
total = 0
while not encerra:
    código = int(input("Digite o código do produto: "))
    qtde = int(input("Digite a quantidade desejada: "))

    if código == 100:
        preço = 1.2
    elif código == 101:
        preço = 1.3
    elif código == 102:
        preço = 1.5
    elif código == 103:
        preço = 1.2
    elif código == 104:
        preço = 1.3
    else:
        preço = 1

    print("Total a ser pago pelo produto:",(preço*qtde))
    total += preço*qtde
    print("Total Geral da conta:",total)

    encerra = bool(int(input("Deseja encerrar a conta (1 - Sim/0 - Não): ")))
