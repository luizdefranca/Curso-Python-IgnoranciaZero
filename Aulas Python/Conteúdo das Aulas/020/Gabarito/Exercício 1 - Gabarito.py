"""
Tendo como dados de entrada a altura e o sexo de uma pessoa,
construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 (h = altura)
Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

altura = float(input("Digite a sua altura: "))
sexo = int(input("Digite o seu sexo(Masculino = 0/ Feminino = 1): "))
peso = float(input("Digite o seu peso: "))

if sexo == 0:
    peso_ideal = (72.7*altura) - 58
else:
    peso_ideal = (62.1*altura) - 44.7

if peso > peso_ideal:
    print("Você está acima do peso")
elif peso == peso_ideal:
    print("Você está no seu peso ideal")
else:
    print("Você está abaixo do peso")

