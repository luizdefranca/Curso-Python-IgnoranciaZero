"""
12.	Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
trabalhadas no mês.

o	Desconto do IR:
o	Salário Bruto até 900 (inclusive) - isento
o	Salário Bruto até 1500 (inclusive) - desconto de 5%
o	Salário Bruto até 2500 (inclusive) - desconto de 10%
o	Salário Bruto acima de 2500 - desconto de 20%

Imprima na tela as informações, dispostas conforme o exemplo abaixo.

No exemplo o valor da hora é 5 e a quantidade de hora é 220.
o	        Salário Bruto: (5 * 220)        : R$ 1100,00
o	        (-) IR (5%)                     : R$   55,00  
o	        (-) INSS ( 10%)                 : R$  110,00
o	        FGTS (11%)                      : R$  121,00
o	        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

"""
valor = float(input("Digite o quanto você ganha por hora: "))
horas = int(input("Digite o número de horas trabalhadas: "))

if 900<horas*valor<=1500:
    desconto = 5
elif 1500< horas*valor <= 2500:
    desconto = 10
elif 2500 < horas*valor:
    desconto = 20

print("Salário Bruto: (%i * %g)\t: R$ %.2f"%(horas, valor, horas*valor))
print("(-) IR (%i%%)\t\t\t: R$ %.2f"%(desconto,horas*valor*desconto/100))
print("(-) INSS ( 10%%)\t\t\t: R$ %.2f"%(horas*valor*0.1))
print("FGTS (11%%)\t\t\t: R$ %.2f"%(horas*valor*0.11))
print("Total de descontos              : R$ %.2f"%(horas*valor*(0.1+desconto/100)))
print("Salário Liquido                 : R$ %.2f"%(horas*valor*(1 - (0.1+desconto/100))))
