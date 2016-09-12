"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 
Segundo Salto: 6.1 
Terceiro Salto: 6.2 
Quarto Salto: 5.4 
Quinto Salto: 5.3 

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

def main():
    """
    Função Principal do Programa
    """
    nome = input("Digite o nome do atleta: ")

    impressão = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

    saltos = []

    for i in range(5):
        salto = float(input(impressão[i] + ' Salto: '))
        saltos.append(salto)

    print("Resultado Final")
    print("Atleta: "+nome)

    imp_salto = "Saltos: "
    for i in range(5):
        imp_salto += str(saltos[i])
        if i == 4:
            break
        imp_salto += ' - '

    print(imp_salto)

    print("Média dos Saltos: ", media(saltos) + 'm')

def media(numeros):
    """
    Calcula a média dos valores de uma dada lista
    """
    soma = 0

    for num in numeros:
        soma += num

    return soma/len(numeros)

main()
