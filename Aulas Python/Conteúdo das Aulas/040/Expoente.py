"""
Escreva uma nested function que forneça um número (x da função menor) elevado
a outro (N da função maior)
"""

def exp(N):
    def eleva(X):
        print(X**N)
    return eleva


