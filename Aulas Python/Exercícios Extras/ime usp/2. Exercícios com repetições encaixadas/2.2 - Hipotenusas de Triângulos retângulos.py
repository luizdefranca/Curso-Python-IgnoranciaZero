"""
Dado um número inteiro positivo n, determinar todos os inteiros entre 1 e n
que são comprimento da hipotenusa de um triângulo retângulo com catetos
inteiros.
"""

hip = int(input("Digite o valor da hipotenusa: "))
cat1, cat2, cont = 3, 4, 1
while cont <= hip:
    while cat1 < hip:
        while cat2 <= hip:
            if cat1**2 + cat2**2 == cont**2 and cat2 > cat1:
                print (cont)
            cat2 += 1
        cat2 = 4
        cat1 += 1
    cat1 = 3
    cat2 = 4
    cont += 1
