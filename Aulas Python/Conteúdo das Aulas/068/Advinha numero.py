"""
Crie o jogo do adivinha número!
Usando os cartões na tupla abaixo, o programa vai pedir para o usuário
pensar em um número entre 1 a 63. Em seguida o programa mostrara um cartão
para o usuário perguntando se o número pensado se encontra nesse cartão.
O usuário deverá digitar sim ou não. Depois de mostrados todos os cartões
o programa deverá mostrar o número que o usuário pensou.

Use o cabeçário da classe jogo para implementar os métodos necessários para rodar o jogo.
Escreve uma excessão SoSimOuNao para verificar a entrada do usuário (coloque-a dentro
de um bloco try).

Um mágico nunca revela seus segredos, por isso veja o método adivinha número na classe jogo
para ver se você consegue descobrir como a adivinhação é feita!
"""

class Jogo(object):
    def __init__(self):
        self.__cartoes = ('''
        1   3   5   7   9   11  13  15
        17  19  21  23  25  27  29  31
        33  35  37  39  41  43  45  47
        49  51  53  55  57  59  61  63
        ''','''
        2   3   6   7   10  11  14  15
        18  19  22  23  26  27  30  31
        34  35  38  39  42  43  46  47
        50  51  54  55  58  59  62  63
        ''','''
        4   5   6   7   12  13  14  15
        20  21  22  23  28  29  30  31
        36  37  38  39  44  45  46  47
        52  53  54  55  60  61  62  63
        ''','''
        8   9   10  11  12  13  14  15
        24  25  26  27  28  29  30  31
        40  41  42  43  44  45  46  47
        56  57  58  59  60  61  62  63
        ''','''
        16  17  18  19  20  21  22  23
        24  25  26  27  28  29  30  31
        48  49  50  51  52  53  54  55
        56  57  58  59  60  61  62  63
        ''','''
        32  33  34  35  36  37  38  39
        40  41  42  43  44  45  46  47
        48  49  50  51  52  53  54  55
        56  57  58  59  60  61  62  63
        ''')
        self.__card = 0
        self.__num = 0
        self.main()


    ############# Métodos a Serem implementadas ###########
    def apresentação(self):
        """
        Método que imprime uma apresentação e explicação rápida de como
        funciona o jogo.
        """
        pass

    def recebeEntradaDoUsuário(self):
        """
        Função que recebe a entrada lida com ela de forma adequada
        Devolve True se o usuário digitou sim e False se digitou não
        """
        pass

    def imprimeNumeroSecreto(self):
        """
        Imprime uma mensagem legal apresentando self.__num
        """
        pass

    ############### Métodos já feitos ###############
    def main(self):
        """
        Método principal do jogo, nele se organiza tudo
        """
        self.apresentação()

        for i in range(len(self.__cartoes)):
            self.__card = i
            self.mostraCartão()
            self.adicionaNumero(self.recebeEntradaDoUsuário())

        self.imprimeNumeroSecreto()


    def mostraCartão(self):
        """
        Escolhe um cartão e o mostra para o usuário
        """
        print(self.__cartoes[self.__card])

    def adicionaNumero(self, esta):
        """
        Adiciona valor ao número secreto
        """
        if esta:
            self.__num += int(self.__cartoes[self.__card].split()[0])



if __name__ == '__main__':
    x = Jogo()

