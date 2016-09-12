def fatorial(n):
    if n==1:
        return n
    return fatorial(n-1) * n


print(fatorial(5))

"""n = 5 --> ret = 1*2*3*4*5
n = 4 --> fatorial(4) = 1*2*3*4
n = 3 --> fatorial(3) = 1*2*3
n = 2 --> fatorial(2) = 1*2
n = 1 --> fatorial(1) = 1"""


print(fatorial(4))
