"""
Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:

 .	A mensagem "Aprovado", se a média for maior ou igual a 7,
        com a respectiva média alcançada;

a.	A mensagem "Reprovado", se a média for menor do que 7,
        com a respectiva média alcançada;

b.	A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

media = float(input("Digite a primeira nota: "))
media += float(input("Digite a segunda nota: "))
media += float(input("Digite a terceira nota: "))

media /= 3
if media == 10:
    print("Aprovado com distanção")
elif media >= 7:
    print("Aprovado.")
    print("Média:", media)
else:
    print("Reprovado.")
    print("Média:", media)


if media >= 7 and media != 10:
    print("Aprovado.")
    print("Média:", media)
elif media < 7:
    print("Reprovado.")
    print("Média:", media)
else:
    print("Aprovado com distanção")
