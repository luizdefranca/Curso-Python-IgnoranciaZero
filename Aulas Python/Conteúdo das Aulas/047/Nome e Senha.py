"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações.
"""
def main():
    nome = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    while tudoMaiusculo(nome) == tudoMaiusculo(senha):
        print("Não aceitamos senhas iguais ao nome de usuário")
        senha = input("Digite a senha: ")


def tudoMaiusculo(string):
    miausculo = ""

    for char in string:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - (ord('a') - ord('A')))
        miausculo += char

    return miausculo

main()
