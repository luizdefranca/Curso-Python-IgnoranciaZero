import random

#random.randrange(start, stop[, step])
"""
Retorna aleatóriamente um elemento de range(começo, fim, passo).
Isso é equivalente a choice(range(começo, fim, passo)), mas não constrói um
objeto range.
"""
#Exemplo
"""
for i in range(10):
    #x = random.randrange(1,7)
    #x = random.randrange(1, 7, 2)
    print(x)
"""

##################################################################

#random.randint(a, b)
"""
Retorna um inteiro N de tal forma que a <= N <= b.
Tal como randrange(a, b+1).
"""
#Exemplo
"""
for i in range(10):
    x = random.randint(1,7)
    print(x)
"""

##################################################################

#random.choice(seq)
"""
Retorna um elemento aleatória de uma sequência não-vazia.
Se recebe uma sequência vazia devolve um erro do tipo IndexError.
"""
#Exemplo
"""
for i in range(10):
    x = random.choice([1.7, 2.3, 3, 4, 5, 6])
    #x = random.choice(range(1, 7))
    print(x)
"""

##################################################################

#random.random()
"""
Retorna um real entre 0.0 e 1.0.
"""
#Exemplo
"""
for i in range(10):
    print(random.random())
"""

##################################################################

#random.uniform(a, b)
"""
Retorna um real N tal que a <= N <= b ou b <= N <= a.
"""
#Exemplo
"""
for i in range(10):
    #x = random.uniform(1, 7)
    #x = random.uniform(7, 1)
    print(x)
"""
