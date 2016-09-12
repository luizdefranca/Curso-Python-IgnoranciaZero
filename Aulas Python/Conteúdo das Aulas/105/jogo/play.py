import sys

sys.path.append('principal')
sys.path.append('constantes')
sys.path.append('objetos')

from jogo import Jogo

try:
    Jogo()
except:
    print(sys.exc_info())
