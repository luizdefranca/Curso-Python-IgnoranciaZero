"""
Bancário. Escreva um programa que registre o caixa de um banco. O programa
começa perguntando se o usuário quer criar uma conta ou fechar o programa. Se
ele escolher fechar o programa escreve uma mensagem de agradecimento e fecha,
caso contrário ele vai pedir que usuário selecione um número com 6 dígitos
e, então, se o número não existir no registro do banco, ele irá pedir um valor
de depósito. Depois o banco perguntara se se deseja ver o saldo do banco, se sim
ele deverá imprimir o balanço geral do banco, senão ele entrará em loop.
"""
contas = []
depositos = []
saldo = 0

def main():
    opção = bool(int(input("Deseja ver o criar conta(1) ou fechar o programa(0): ")))
    while opção:
        criaConta()
        VerSaldo()
        opção = bool(int(input("Deseja ver o criar conta(1) ou fechar o programa(0): ")))

def criaConta():
    global contas, depositos, saldo
    num_conta = int(input("Digite um número de conta: "))

    while num_conta in contas:
        print("Conta já existente. Digite novamente.")
        num_conta = int(input("Digite um número de conta: "))

    contas.append(num_conta)

    deposito = float(input("Digite o valor do seu primeiro depósito: "))
    while deposito <= 0:
        print("Valor de depósito inválido.")
        deposito = float(input("Digite o valor do seu primeiro depósito: "))

    depositos.append(deposito)
    saldo += deposito

def VerSaldo():
    global saldo
    opção = bool(int(input("Deseja ver o saldo do banco(1 - Sim/ 0 - Não): ")))
    if opção:
        print("O saldo do banco é R$", saldo)


main()
