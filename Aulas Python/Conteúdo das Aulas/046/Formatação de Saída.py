"""
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo
de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo
desses carros, isto é, quantos quilômetros cada um desses carros faz com um
litro de combustível. Calcule e mostre:

a.	O modelo do carro mais econômico;
b.	Quantos litros de combustível cada um dos carros cadastrados consome
para percorrer uma distância de 1000 quilômetros e quanto isto custará,
considerando um que a gasolina custe R$ 2,25 o litro.

Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais
próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada
execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: vectra
Km por litro: 9
Veículo 5
Nome: peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""
def main():
    print("Comparativo de Consumo de Combustível\n")

    lista = []

    for i in range(5):
        print("Veículo %i"%(i+1))
        nome = input("Nome: ")
        km = float(input("Km por Litro: "))
        lista.append([nome, km])

    print("\nRelatório Final")

    saidas = []

    for i in range(5):
        saidas.append(' %i - '%(i+1))
        
        #Nomes
        x = lista[i][0]
        Formata1(i, x, 16, saidas)

        saidas[i] +=' - '

        #Km por litro
        x = "%.1f"%lista[i][1]
        Formata2(i, x, 6, saidas)

        saidas[i] +=' - '

        #Litros a cada mil km
        x = "%.1f"%(1000/lista[i][1])
        Formata2(i, x, 6, saidas)

        saidas[i] += " litros - R$ "

        #R$ a cada mil km
        x = "%.2f"%(2250/lista[i][1])
        Formata2(i, x, 6, saidas)

        #Imprimindo Tudo
        print(saidas[i])


def Formata1(i, palavra, lmt, saida):
    if len(palavra) <= lmt:
        saida[i] += palavra + (lmt - len(palavra))*" "
        

def Formata2(i, palavra, lmt, saida):
    if len(palavra) <= lmt:
        saida[i] += (lmt - len(palavra))*" " + palavra

main()



    






