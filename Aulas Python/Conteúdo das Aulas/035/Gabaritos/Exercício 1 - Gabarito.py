"""
Escreva uma função que obtenha a multiplicação de vários números de entrada
"""

def mult(*nums):
    prod = 1
    for num in nums:
        prod*=num

    return prod
