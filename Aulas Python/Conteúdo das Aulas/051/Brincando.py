"""
arquivo = open('OlaArquivo.txt', 'w')

# 'w' --> write --> escrever
# 'r' --> read --> ler
# 'a' --> append --> extender

arquivo.write('Chiclete com Banana')
arquivo.write('\n')
arquivo.write('Manga com Leite')

#arquivo.writelines(['Ola', 'arquivo', 'essa', 'eh', 'nossa', 'primeira', 'aula'])

arquivo.close()
"""

"""
arquivo = open('OlaArquivo.txt', 'r')
arquivo.readline()
x = arquivo.readlines()
print(x)

arquivo.close()
"""
arquivo = open('OlaArquivo.txt', 'a')
arquivo.write('\nNova linha')
arquivo.close()


