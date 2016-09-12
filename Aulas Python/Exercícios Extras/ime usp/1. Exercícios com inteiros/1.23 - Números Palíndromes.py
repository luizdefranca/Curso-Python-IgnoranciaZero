"""
Dizemos que um número natural n é palíndromo (3) se 
    o 1º algarismo de n é igual ao seu último algarismo, 
    o 2º algarismo de n é igual ao penúltimo algarismo, 
    e assim sucessivamente.

Exemplos:
567765 e 32423 são palíndromos.
567675 não é palíndromo.
Dado um número natural   n > 10 , verificar se n é palíndrome.
"""

n = int(input("Digite um número: "))
aux = n
reverso = 0

while aux != 0:
    reverso = reverso*10 + aux%10
    aux //= 10

if reverso == n:
    print(n,"é palindrome")
else:
    print(n,"não é palindrome")

