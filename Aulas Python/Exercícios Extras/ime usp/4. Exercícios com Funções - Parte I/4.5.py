def main ():
    n = int(input("Digite n: "))
    a = int(input("Digite o número 1 de %d: "%(n)))
    for i in range (1,n):
        b = int(input("Digite o número %d de %d: "%(i+1,n)))
        a = euclides(a,b)
    print(a)

def euclides(a,b):
    r = a%b
    while r!=0:
        a = b
        b = r
        r = a%b
    return b
main ()
