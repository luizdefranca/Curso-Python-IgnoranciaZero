"""
40.	Foi feita uma estatística em cinco cidades brasileiras para coletar
dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

 .	Código da cidade;
a.	Número de veículos de passeio (em 1999);
b.	Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
c.	Qual o maior e menor índice de acidentes de transito e a que cidade
        pertence;

d.	Qual a média de veículos nas cinco cidades juntas;

e.	Qual a média de acidentes de trânsito nas cidades com menos de 2.000
        veículos de passeio.

"""
cod_menor = cod_maior = int(input("Digite o código da cidade: "))
media_veic = int(input("Número de veículos de passeio: "))
acid_maior = acid_menor = int(input("Digite o número de acidentes: "))
media_acid = cont = 0
if media_veic < 2000:
    media_acid += acid_maior
    cont += 1

for i in range(4):
    cod = int(input("Digite o código da cidade: "))
    veic = int(input("Número de veículos de passeio: "))
    acid = int(input("Digite o número de acidentes: "))

    if veic < 2000:
        media_acid += acid
        cont += 1

    media_veic += veic

    if acid < acid_menor:
        cod_menor = cod
        acid_menor = acid

    if acid > acid_maior:
        cod_maior = cod
        acid_maior = acid

if cont > 0:
    media_acid /= cont

media_veic /= 5

print("O maior índice de acidentes (%i) pertence a cidade %i"%(acid_maior, cod_maior))
print("O menor índice de acidentes (%i) pertence a cidade %i"%(acid_menor, cod_menor))
print("Média de Veículos: %g"%media_veic)
print("Média de acidentes nas cidades com menos de 2000 veículos: %g"%(media_acid))
    
