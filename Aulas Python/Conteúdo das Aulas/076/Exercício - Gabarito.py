"""
Crie um database de sites permitindo que o usuário
acesse esse database recupere a descriçao de cada site
e tambem coloque novos sites. Tenha certeza que as entradas do
usuário para sites sejam válidas, www.nomedosite.com
"""
import dbm

class EntradaErro(Exception):
    def __init__(self, site):
        self.entrada = site

    def verificaEntrada(self):
        divisao = self.entrada.split('.')
        try:
            if divisao[0] != 'www' or (divisao[2] != 'com' and divisao[2] != 'org'):
                raise self
        except IndexError:
            raise self

    def __str__(self):
        return 'A entrada %s não é válida'%self.entrada

class ManipulaDB(object):
    def __init__(self, db):
        self.db = db
        self.main()
        
    def main(self):
        while True:
            d = self.recebeEntradaDoUsuário()

            if d.startswith('a'):
                self.pegaValor()
            else:
                self.colocaChave()
        
    def recebeEntradaDoUsuário(self):
        while True:
            decisao = input('Deseja abrir um site(a/abrir) ou colocar uma nova entrada(e/entrada)?\n').lower()
            if not decisao.isalpha():
                print('Digite apenas letras')
            elif decisao.startswith('a') or decisao.startswith('e'):
                return decisao
            else:
                print('Entrada inválida')

    def pegaValor(self):
        chave = input('Digite o nome do site\n')

        for key in self.db:
            if key.decode().lower() == chave.lower():
                print(self.db[key].decode())
                return
        print('Site não encontrado!!')

    def colocaChave(self):
        nome = input('Digite o nome do site\n')
        while True:
            site = input('Digite o endereço do site\n')
            try:
                EntradaErro(site).verificaEntrada()
            except EntradaErro as E:
                print(E)
            else:
                break
        self.db[nome] = site
        
        
if __name__ == '__main__':
    #Para python 3.4
    #with dbm.open('sites', 'c') as db:
    #    ManipulaDB(db)
    try:
        db = dbm.open('sites', 'c')
    except IOError:
        print('Erro ao abrir database')
    else:
        ManipulaDB(db)
            
        
