"""
 Dados n e uma seqüência de n números inteiros, determinar o comprimento de
 um segmento crescente de comprimento máximo.

Exemplos:
Na seqüência   5,  10,  3,  2,  4,  7,  9,  8,  5
o comprimento do segmento crescente máximo é 4.

Na seqüência   10,  8,  7,  5,  2
o comprimento de um segmento crescente máximo é 1.
"""

n = int(input("Digite o tamanho da sequência: "))
cont, seg, arm_prim = 1, 1, 1
ant = int(input("Digite um número da sequência: "))
while cont < n:
    num = int(input("Digite um número da sequência: "))
    if num > ant:
        seg += 1
    else:
        if seg > arm_prim:
            arm_prim = seg
        seg = 1

    ant = num
    cont += 1
print ("O maior segmento é de",arm_prim)
