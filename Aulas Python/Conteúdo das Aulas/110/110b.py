##### Streams - Redirecionamento #####

import os, sys

com_win = ["python interect.py", "type input.txt", "python interect.py < input.txt", "python interect.py < input.txt > output.txt"]
com_unix = ["python3 interect.py", "cat input.txt", "python3 interect.py < input.txt", "python3 interect.py < input.txt > output.txt"]

if 'win' in sys.platform:
    com = com_win
else:
    com = com_unix

print("Execução do arquivo interect: " + "\n")
os.system(com[0])
input("Acabou com o interect ")
print()

print("Leitura do arquivo input.txt: ")
os.system(com[1])
input("Acabou a leitura ")
print()

print("Execução do arquivo a interect a partir da entrada do input.txt: " + "\n")
os.system(com[2])
input("Acabou a Execução ")
print()

print("Execução do arquivo a interect a partir da entrada do input.txt com saída em output.txt: " + "\n")
os.system(com[3])
input("Acabou a Execução ")
