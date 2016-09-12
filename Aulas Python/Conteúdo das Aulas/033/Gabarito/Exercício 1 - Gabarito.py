"""
Faça um programa com uma função chamada somaImposto.

A função possui dois parâmetros formais:
    1 - taxaImposto, que é a quantia de imposto sobre vendas expressa em
        porcentagem
    2 - custo, que é o custo de um item antes do imposto.

A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(taxaImposto, custo):
    return custo*(1 + taxaImposto/100)

custo_normal = float(input("Digite o custo(R$): "))
taxa = float(input("Digite a taxa de imposto(%): "))

print("O custo recalculado com o imposto é de R$%.2f"%somaImposto(custo_normal, taxa))
