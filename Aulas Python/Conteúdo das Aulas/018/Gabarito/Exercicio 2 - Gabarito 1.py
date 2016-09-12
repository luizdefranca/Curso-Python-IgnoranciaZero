"""
Sabe-se que um número da forma n**3 é igual a soma de n ímpares consecutivos.

Exemplo: 1**3= 1, 2**3= 3+5, 3**3= 7+9+11,  4**3= 13+15+17+19,...
Dado m, determine os ímpares consecutivos cuja soma é igual a n**3 para n
assumindo valores de 1 a m. 
"""

m = int(input("Digite o valor de m: "))
for n in range(1, m+1):
    soma, inicio = 0, 1
    while soma != n*n*n:
        soma = 0
        for i in range(n):
            soma = soma + inicio + 2 * i
        inicio += 2

    inicio = inicio - 2
    print("%d*%d*%d = "%(n, n, n))
    for i in range(n):
      print("+", inicio+2*i)
    print("\n")
