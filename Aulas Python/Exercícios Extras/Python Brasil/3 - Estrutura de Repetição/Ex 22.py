"""
Altere o programa de cálculo dos números primos, informando,
caso o número não seja primo, por quais número ele é divisível.
"""
p = int(input("Digite p: "))
k = 2
while k < p:
    if p % k == 0:
        print (p, "não é primo.")
        cont = 1
        print(p, "é divisivel por: ")
        while cont <= p:
            if p % cont == 0:
                print("    ",cont)
            cont += 1
        k = p
    k += 1
if k == p:
    print (p, "é primo.")
