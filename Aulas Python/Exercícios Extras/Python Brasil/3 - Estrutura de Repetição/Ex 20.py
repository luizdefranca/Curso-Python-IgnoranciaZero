"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos
e menores que 16.
"""
acabou = False
while acabou != True:
    ok = False
    while ok == False:
        n = int(input("Digite n: "))
        if 0< n < 16:
            ok = True
        else:
            print("Entrada invalida, digite um numero entre 0 e 16")
    
    cont = 1
    prod = 1
    while cont < n:
        prod = prod * (cont + 1)
        cont = cont + 1
    
    print ("O valor de", n, "! é igual a", prod)

    acabou = bool(int(input("Deseja calcular outro fatorial(0 - Sim/1 - Não): ")))
