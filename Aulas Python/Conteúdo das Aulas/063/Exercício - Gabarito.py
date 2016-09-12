"""
Escreva um programa de bancos que possua:
    Uma classe Banco com os atributos
    - private total
    - public TaxaReserva
    - private reservaExigida

    E métodos
    - public podeFazerEmprestimo(valor) --> bool
    - public MudaTotal(valor)

E uma classe conta com os atributos
    - private saldo
    - private ID
    - private senha

    E métodos
    - public deposito(senha, valor)
    - public saque(senha, valor)
    - public podeReceberEmprestimo(valor) --> bool
    - public saldo --> float
"""

class Banco(object):
    __total = 10000
    TaxaReserva = 0.1
    reservaExigida = __total*TaxaReserva

    def podeFazerEmprestimo(valor):
        Banco.__total -= valor
        if Banco.__total >= Banco.reservaExigida:
            pode = True
        else:
            pode = False

        Banco.__total += valor

        return pode

    def MudaTotal(valor):
        Banco.__total += valor

class Conta
    def __init__(self, saldo, ID, senha):
        self.__saldo = saldo
        self.__ID = ID
        self.__senha = senha

    def deposito(self, senha, valor):
        if senha == self.__senha:
            self.__saldo += valor
            Banco.mudaTotal(valor)

    def saque(self, senha, valor):
        if senha == self.__senha:
            self.__saldo -= valor
            Banco.mudaTotal(-valor)

    def podeReceberEmprestimo(self, valor):
        return Banco.podeFazerEmprestimo(valor)

    def saldo(self):
        print(self.__saldo)
