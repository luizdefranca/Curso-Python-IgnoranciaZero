def main ():
    n = int(input("Digite o número de alunos: "))
    k = int(input("Digite o número de provas: "))
    p = []
    geral1 = []
    f(k, p, geral1)
    geral2 = []
    for i in range (n):
        a = []
        nota, div = 0.0, 0.0
        f (k, a, geral2)
        for j in range (k):
            nota += p[j]*a[j]
            div += p[j]
        media = nota/div
        print ("Média do aluno%d: %.2f"%(i+1, media))
    media2 = []
    for i in range (k):
        media2.append(geral2[i]/n)
    print("Média das provas: ", media2)

def f(k, a, geral):
    for i in range (k):
        ele = float(input("Digite a nota ou peso da prova %d de %d: "%(i+1, k)))
        a.append(ele)
        if len(geral) < k:
            geral.append(ele)
        else:
            geral[i] += ele
    return a, geral
main ()
        
        
        
            
