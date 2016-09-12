"""
31.	O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de
1,99 e agora possui uma loja de conveniências.

Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos
preços das mercadorias. Um valor zero deve ser informado pelo operador para
indicar o final da compra. O programa deve então mostrar o total da compra e
perguntar o valor em dinheiro que o cliente forneceu, para então calcular e
mostrar o valor do troco. Após esta operação, o programa deverá voltar ao
ponto inicial, para registrar a próxima compra. A saída deve ser conforme o
exemplo abaixo:

o	Lojas Tabajara 
o	Produto 1: R$ 2.20
o	Produto 2: R$ 5.80
o	Produto 3: R$ 0
o	Total: R$ 9.00
o	Dinheiro: R$ 20.00
o	Troco: R$ 11.00
o	...

"""

print("Lojas Tabajara")

while True:
    produto = float(input("Produto 1: R$ "))
    total, cont = 0, 2
    while produto != 0:
        total += produto
        produto = float(input("Produto %i: R$ "%cont))
        cont += 1

    print("Total: R$ %.2f"%total)
    dinheiro = float(input("Dinheiro: R$ "))
    print("Troco: R$ %.2f"%(dinheiro - total))
