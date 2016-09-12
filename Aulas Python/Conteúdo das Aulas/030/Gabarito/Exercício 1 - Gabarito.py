"""
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando
for informado um valor igual a -1 (que não deve ser armazenado).
Após esta entrada de dados, faça:
a.	Mostre a quantidade de valores que foram lidos;
b.	Exiba todos os valores na ordem em que foram informados;
c.	Exiba todos os valores na ordem inversa à que foram informados;
d.	Calcule e mostre a soma dos valores;
e.	Calcule e mostre a média dos valores;
f.	Calcule e mostre a quantidade de valores acima da média calculada;
g.	Calcule e mostre a quantidade de valores abaixo de sete;
h.	Encerre o programa com uma mensagem;
"""

notas = []

nota = float(input("Digite uma nota: "))

while nota != -1:
    notas.append(nota)
    nota = float(input("Digite uma nota: "))

print("Foram lidos %i valores."%len(notas))

print("\nValores informados: ")
for nota in notas:
    print(nota)

print("\nValores informados(ordem inversa): ")
notas.reverse()
for nota in notas:
    print(nota)

soma = 0
for nota in notas:
    soma += nota
print("\nA soma de valores é", soma)

soma /= len(notas)
print("\nA média dos valores é", soma)

acima = 0
for nota in notas:
    if nota > soma:
        acima += 1
print("\nNúmero de notas acima da média é", acima)

abaixo = 0
for nota in notas:
    if nota < 7:
        abaixo += 1
print("\nNúmero de notas abaixo de 7 é", abaixo)

print("\nÉ isso ai pessoal!")

#Detalhe: Podemos calcurar todas essa informações em um
#número bem menor de for loops do que o que foi colocado


