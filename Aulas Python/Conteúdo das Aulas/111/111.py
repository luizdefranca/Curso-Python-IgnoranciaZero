import os, sys

com_win = ["type escreve.py", "type recebe.py", "python escreve.py", "python escreve.py | python recebe.py"]
com_unix = ["cat escreve.py", "cat recebe.py", "python3 escreve.py", "python3 escreve.py | python3 recebe.py"]

if "win" in sys.platform:
    com = com_win
else:
    com = com_unix

print("Le arquivo escreve.py: ")
os.system(com[0])
input()

print("Le arquivo recebe.py: ")
os.system(com[1])
input()

print("Executs escreve.py: ")
os.system(com[2])
input()

print("Executs escreve.py e manda sua saída por um pipe para recebe.py: ")
os.system(com[3])
input()

