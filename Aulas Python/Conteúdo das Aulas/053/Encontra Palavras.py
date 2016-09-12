def GeraDicionário():
    """
    Carrega o arquivo com a lista de palavras e com isso
    gera um dicionário, que é uma lista contendo todas as
    palavras, e a devolve
    """

def RecebeFrase():
    """
    Das letras que recebemos temos que garantir nenhuma tenha
    acento ou ç
    """

def ProcuraPalavra(dicionário, palavra):
    """
    Procura as possíveis palavras para substituir
    a palavra passada, e as devolve numa lista
    """
    
    
def SeparaPorTamanho(dicionário, palavra):
    """
    Separa as possíveis candidatas a palavras substitutas
    por tamanho
    """
    

def GeraFrasesPossíveis(candidatas_totais):
    """
    A partir da matriz com todas as palavras candidatas
    essa função vai gerar todas as possíveis frases
    """

    aux = open('auxiliar.py', 'w')
    aux.write('def funcao_auxiliar(candidatas_totais):\n')
    aux.write('\tarquivo = open("FRASE.txt", "w")\n')

    aux.write('\tfrase = []\n')
    aux.write('\tfor i in range(len(candidatas_totais)):\n')
    aux.write('\t\tfrase.append("")\n')

    for i in range(len(candidatas_totais)):
        linha = '\t'*(i+1)
        linha += 'for a%i in range(len(candidatas_totais[%i])):\n'%(i,i)
        aux.write(linha)
        linha = '\t'*(i+2) + 'frase[%i]= candidatas_totais[%i][a%i]\n'%(i,i,i)
        aux.write(linha)

    aux.write('\t'*(i+2) + 'frase_s = ""\n')
    aux.write('\t'*(i+2) + 'for palavra in frase:\n')
    aux.write('\t'*(i+3)+ 'frase_s += palavra\n')
    aux.write('\t'*(i+3)+ 'frase_s += " "\n')
    aux.write('\t'*(i+2) + 'arquivo.write(frase_s + "\\n")\n')

    aux.write('\tarquivo.close()')

    aux.close()

    print("Gerando Lista de Palavras Candidatas...")
    
    from auxiliar import funcao_auxiliar

    funcao_auxiliar(candidatas_totais)     

def main():
    """
    Função principal do programa
    """

main()

    
