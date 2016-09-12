import csv

print("O módulo csv permite lidar com tabelas")
print("desse tipo de uma maneira bastante")
print("simples")

input()

f = open('tabela.csv', 'w')
try:
    writer = csv.writer(f)
    writer.writerow( ('Nome','Idade','Sexo') )
    writer.writerow( ('Lucas', 15, 'M') )
    writer.writerow( ('Luana', 16, 'F') )
    writer.writerow( ('João', 15, 'M') )
finally:
    f.close()

print(open('tabela.csv', 'r').read())


input()

f = open('tabela.csv', 'r')
try:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
finally:
    f.close()

input()

f = open('tabela.csv', 'a')
try:
    writer = csv.writer(f)
    writer.writerow( ('Luciana', '19', 'F') )
    writer.writerow( ('Felipe', '13', 'M') )
finally:
    f.close()

print(open('tabela.csv', 'rt').read())

input()
