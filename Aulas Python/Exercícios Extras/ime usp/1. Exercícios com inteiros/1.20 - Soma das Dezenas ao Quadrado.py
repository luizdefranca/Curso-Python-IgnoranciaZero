"""
Qualquer número natural de quatro algarismos pode ser dividido em duas dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.

Exemplos:
1297: 12 e 97.
5314: 53 e 14.

Escreva um programa que imprime todos os milhares (4 algarismos)
cuja raiz quadrada seja a soma das dezenas formadas pela divisão acima.
    Exemplo: raiz de 9801 = 99 = 98 + 01. 
    Portanto 9801 é um dos números a ser impresso.
"""

cont = 1000
while cont < 10000:
    n = cont
    dez = n % 100
    n = n // 100
    cent = n % 100
    if (dez + cent)**2 == cont:
        print (cont)
    cont += 1
