"""
Faça um Programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o preço seja o menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
"""

area = float(input("Digite o tamanho da área: "))

#Acrescentamos os 10% de folga
area *= 1.1

#Agora vamos arredondar a área da seguinte maneira
excesso = area - int(area) #aqui estamos pegando as casas decimais da area
area = int(area) #Aqui retiramos a parte inteira da area

if excesso > 0:
    area += 1 #sempre devemos arredondar para cima

#Vamos calcular o numero de litros necessários para pintar a casa
litros = area//6
if area % 6 > 0:
    litros += 1

print("Litros necessários:", litros,"\n")

print("1) comprar apenas latas de 18 litros")
latas = litros//18
if litros % 18 > 0:
    latas += 1

print("Serão necessárias", latas, "latas")
print("Obteremos", latas*18, "litros")
print("Total: R$", latas*80)

print("\n2)Comprar apenas galões de 3,6 litros")
galoes = litros//3.6
if litros % 3.6 > 0:
    galoes += 1

print("Serão necessárias", galoes, "galoes")
print("Obteremos", galoes*3.6, "litros")
print("Total: R$", galoes*25)

#Vamos pensar, o preço total por litro pago nas latas é 80/18 ~ 4.44 R$/L
#enquanto que para o gualão é 25/3.6 ~ 6.94 R$/L
#portanto é sempre mais vantajoso comprar o máximo de latas possíveis
#e o mínimo de galões, desde que o preço desses galoes não ultrapasse o preço
#de uma lata, isto é, o numero de galoes seja menor ou igual a 3 (R$ 75)
print("\n3)Misturar latas e galões, de forma que o preço seja o menor.")
latas = litros//18
litros_restantes = litros%18

if litros_restantes <= 3*3.6:
    #Ou seja o numero de galoes necessarios seja menor do que três
    galoes = litros_restantes // 3.6
    if litros_restantes % 3.6 > 0:
        galoes += 1

print("Serão necessárias", latas, "latas")
print("Serão necessárias", galoes, "galoes")
print("Obteremos", latas*18 + galoes*3.6, "litros")
print("Total: R$", galoes*25 + latas*80)
