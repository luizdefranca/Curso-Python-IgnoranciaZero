"""
Classe Ponto e Retangulo:
Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior
esquerdo do retângulo, que deve ser um objeto da classe Ponto.

A função para encontrar o centro do retângulo deve retornar o valor para um
objeto do tipo ponto que indique os valores de x e y para o centro do objeto.

O valor do centro do objeto deve ser mostrado na tela

Crie um menu para alterar os valores do retângulo e imprimir o centro deste
retângulo.
"""

class Ponto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def imprime(self):
        print("Ponto (%g,%g)"%(self.x, self.y))

class Retangulo:
    def __init__(self, ponto = Ponto(), b = 0, h = 0):
        self.largura = b
        self.altura = h
        self.verticePartida = ponto

    def encontraCentro(self):
        x = self.verticePartida.x + self.largura/2
        y = self.verticePartida.y + self.altura/2

        return Ponto(x, y)

def main():
    verticePartida = Ponto()
    rect = Retangulo()
    
    while True:
        comando = Menu()

        if comando.startswith('m'):
            mudaValores(rect)
        elif comando.startswith('i'):
            rect.encontraCentro().imprime()
        else:
            break

def Menu():
    while True:
        comando = input('Deseja mudar os valores do retângulo(m/mudar), imprimir seu centro(i/imprimir) ou fechar o programa(f/fechar)?\n')

        comando.lower()

        if not comando.isalpha():
            print('Digite apenas letras!')
        else:
            if comando.startswith('m') or comando.startswith('i') or comando.startswith('f'):
                return comando
            else:
                print('Não entendi seu comando, digite novamente')

def mudaValores(rect):
    rect.largura = float(input('Digite o valor da largura:\n'))
    rect.altura = float(input('Digite o valor da altura:\n'))
    rect.verticePartida.x = float(input('Digite o valor do x do vértice de partida:\n'))
    rect.verticePartida.y = float(input('Digite o valor do y do vértice de partida:\n'))

main()

    

    
