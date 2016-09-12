"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
x = input("Digite uma letra: ")

if x == 'M' or x == 'm':
    print("M - Masculino")
elif x == 'F' or x == 'f':
    print('F - Feminino')
else:
    print("Entrada invalida")
