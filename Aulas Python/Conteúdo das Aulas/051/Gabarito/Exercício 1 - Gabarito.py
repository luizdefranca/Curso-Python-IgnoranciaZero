"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em
disco no seu servidor de arquivos. Para tentar resolver este problema, o
Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e
identificar os usuários com maior espaço ocupado. Através de um programa,
baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado
"usuarios.txt":

alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo,
você deve criar um programa que gere um relatório, chamado "relatório.txt", no
seguinte formato:

ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em
memória, caso sejam necessários, de forma a agilizar a execução do programa.
A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita
através de uma função separada, que será chamada pelo programa principal.
O cálculo do percentual de uso também deverá ser feito através de uma função,
que será chamada pelo programa principal.
"""

def main():
    arquivo = open("usuarios.txt", 'r')

    linha = arquivo.readline()

    espaçoTotal = 0
    usuarios = []

    while linha != '':
        separado = linha.split()
        removeEspaços(separado)

        espaçoTotal += int(separado[1])

        usuarios.append(separado)

        linha = arquivo.readline()

    arquivo.close()

    espaçoTotal /= (1024**2)

    geraRelatorio(usuarios, espaçoTotal)

def removeEspaços(splited):
    while splited.count('') != 0:
        splited.remove('')

def geraRelatorio(usuarios, espaçoTotal):
    relatorio = open('relatorio.txt', 'w')

    CalculaEspaçoUtilizado(usuarios)
    porc = CalculaPorcentagem(usuarios, espaçoTotal)

    relatorio.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    relatorio.write(72*'-' + '\n')
    relatorio.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    maior = EspaçosASeremColocados(usuarios)

    relatorio.write('\n')
    
    for i in range(len(usuarios)):
        linha = '%i'%(i+1)
        linha += (5-len(linha))*' '

        linha += usuarios[i][0] + (15 - len(usuarios[i][0]))*' '

        num = "%.2f"%usuarios[i][1]
        espaço_inicio = (maior - len(num))*' '
        num += ' MB'
        espaço_fim = (23 - len(espaço_inicio)-len(num))*' '
        linha += espaço_inicio + num + espaço_fim

        porcentagem = "%.2f"%porc[i]
        espaço_inicio = (5 - len(porcentagem))*' '
        linha += espaço_inicio + porcentagem + "%"

        relatorio.writelines(linha + '\n')

    relatorio.write('\n')
    relatorio.write('Espaço total ocupado: %.2f'%espaçoTotal + '\n')
    relatorio.write('Espaço médio ocupado: %.2f'%(espaçoTotal/len(usuarios)) + '\n')
    relatorio.close()

def CalculaEspaçoUtilizado(usuarios):
    for i in range(len(usuarios)):
        usuarios[i][1] = float(usuarios[i][1])/(1024**2)

def CalculaPorcentagem(usuarios, espaçoTotal):
    porc = []
    for usuario in usuarios:
        porc.append(100*usuario[1]/espaçoTotal)

    return porc

def EspaçosASeremColocados(usuarios):
    maior_string = 0
    for usuario in usuarios:
        if len("%.2f"%usuario[1]) > maior_string:
            maior_string = len("%.2f"%usuario[1])

    return maior_string
    
main()

    

