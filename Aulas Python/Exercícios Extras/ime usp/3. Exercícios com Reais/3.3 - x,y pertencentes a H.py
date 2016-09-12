n = int(input("Digite n: "))
for i in range (n):
    x = float(input("Digite a abcissa %d de %d: "%(i+1, n)))
    y = float(input("Digite a ordenada %d de %d: "%(i+1, n)))
    ponto = []
    ponto.append(x)
    ponto.append(y)
    if x*x + y*y <= 1:
        print("O ponto", ponto, "pertence a H")
    else:
        print("O ponto", ponto, "não pertence a H")
