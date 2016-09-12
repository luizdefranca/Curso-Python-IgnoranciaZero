"""
Escreva uma função recursiva que imprima de um número x até um y
"""

def funçãoRecursiva(x, y):
    if x <= y:
        print(x)
        funçãoRecursiva(x + 1, y)

funçãoRecursiva(0, 10)
   
