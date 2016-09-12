def main():
    p = f()
    q = f()
    pXq = []
    for j in range (len(q)):
        ele = p[0]*q[j]
        pXq.append(ele)
    for r in range (1, len(p)):
        for s in range (len(q)):
            if r+s <= (len(pXq) - 1):
                pXq[r+s] += p[r]*q[s]
            else:
                pXq.append(p[r]*q[s])
    print (pXq)
def f():
    poli = []
    n = int(input("Digite o grau do polinômio: "))
    for i in range (n+1):
        a = float(input("Digite o a%d: "%(i)))
        poli.append(a)
    return poli
main ()
