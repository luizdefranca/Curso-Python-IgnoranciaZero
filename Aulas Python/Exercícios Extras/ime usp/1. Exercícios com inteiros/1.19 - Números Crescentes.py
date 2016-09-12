"""
Dados três números, imprimi-los em ordem crescente. 
"""

n = int(input("Digite um número: "))
p = int(input("Digite um número: "))
q = int(input("Digite um número: "))
if n > p > q:
    print (n, ">", p,">", q)
elif n > q > p:
    print (n, ">", q,">", p)
elif p > n > q:
    print (p, ">", n,">", q)
elif p > q > n:
    print (p, ">", q,">", n)
elif q > n > p:
    print (q, ">", n,">", p)
else:
    print (q, ">", p,">", n)
