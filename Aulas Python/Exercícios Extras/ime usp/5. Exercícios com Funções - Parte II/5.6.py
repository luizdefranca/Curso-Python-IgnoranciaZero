def main ():
    n = int(input("Digite n: "))
    Fn_2, Gn_2 = valor (n-2)
    Fn_200, Gn_200 = valor (n+200)
    A = Fn_2 + Gn_200
    B = Fn_200 - Gn_2
    print (A, B)
def valor (k):
    F1, F2, G2, G1 = 2, 1, 2, 1
    if k==1:
        F = F1
        G = G1
    elif k == 2:
        F = F2
        G = G2
    else:
        for i in range (k):
            F = 2*F2 + G1
            G = G2 + 3*F1
            F2, F1, G2, G1 = F, F2, G, G2
    return F,G
main ()
