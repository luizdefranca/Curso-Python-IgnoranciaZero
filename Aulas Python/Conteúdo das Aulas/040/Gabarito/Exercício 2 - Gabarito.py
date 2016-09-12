"""
Reescreva o programa bancário da aula 36 colocando todas as funções dentro da
função main. Utilize o statement nonlocal.
(OBS: Pense bem onde colocar as variáveis "globais")
"""

def main():
    """
    Função principal do programa. Possui duas nested functions:
    criaConta e VerSaldo
    """
    contas = []
    depositos = []
    saldo = 0
    
    def criaConta():
        """
        Cria uma nova conta
        """
        nonlocal contas, depositos, saldo
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
        """
        Permite que o usuário visualize seu saldo
        """
        #nonlocal saldo --> Note que não é preciso colocar nonlocal
        #já que não modificamos o valor de saldo
        opção = bool(int(input("Deseja ver o saldo do banco(1 - Sim/ 0 - Não): ")))
        if opção:
            print("O saldo do banco é R$", saldo)



    opção = bool(int(input("Deseja ver o criar conta(1) ou fechar o programa(0): ")))
    while opção:
        criaConta()
        VerSaldo()
        opção = bool(int(input("Deseja ver o criar conta(1) ou fechar o programa(0): ")))

main()
