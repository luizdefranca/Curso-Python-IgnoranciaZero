"""
11.	As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.

o	Faça um programa que recebe o salário de um colaborador e o
        reajuste segundo o seguinte critério, baseado no salário atual:

o	salários até R$ 280,00 (incluindo) : aumento de 20%
o	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o	salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:
o	o salário antes do reajuste;
o	o percentual de aumento aplicado;
o	o valor do aumento;
o	o novo salário, após o aumento.

"""
salário = float(input("Digite o seu salário: "))
if salário <= 280:
    percentual = 20
elif 280 < salário <= 700:
    percentual = 15
elif 700 < salário <= 1500:
    percentual = 10
else:
    percentual = 5

print("Salário inicial: R$%.2f"%salário)
print("Percentual aplicado: %%%i"%percentual)
print("Valor do aumento: R$%.2f"%(salário*percentual/100))
print("Novo salário: R$%g"%(salário*(1+percentual/100)))
