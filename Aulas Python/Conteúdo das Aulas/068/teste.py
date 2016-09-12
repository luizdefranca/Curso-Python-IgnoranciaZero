
class ValorRepetidoErro(Exception):
    def __init__(self, n):
        self.num = n
    def __str__(self):
        return 'Putz meu caro, você já digitou esse %i antes'%self.num

def main():
    lista = []

    for i in range(3):
        while True:
            try:
                num = int(input('Escolher um número: '))
                break
            except ValueError:
                print('Digite apenas números!')

        if num not in lista:
            lista.append(num)
        else:
            raise ValorRepetidoErro(num)
        
        


if __name__ == '__main__':
    main()
