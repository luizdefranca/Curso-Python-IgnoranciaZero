import os, sys

if "win" in sys.platform:
    os.system("python aleatorio.py > dados.txt")
    os.system("python arruma.py < dados.txt | python maximo.py")
else:
    os.system("python3 aleatorio.py > dados.txt")
    os.system("python3 arruma.py < dados.txt | python3 maximo.py")
