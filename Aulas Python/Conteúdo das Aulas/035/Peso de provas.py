"""
Exemplo: Peso de provas
"""
def soma(*nums):
    soma_num = 0
    for num in nums:
        soma_num += num

    return soma_num

def media(p1, p2, p3, peso1 = 1, peso2 = 1, peso3 = 1):
    return(p1*peso1 + p2*peso2 + p3*peso3)/soma(peso1, peso2, peso3)

print(media(6, 4, 5, 2))
