n = int(input("Digite n: "))
freq = 0
for i in range (n):
    x = float(input("Digite a abcissa %d de %d: "%(i+1, n)))
    y = float(input("Digite a ordenada %d de %d: "%(i+1, n)))
    ponto = []
    ponto.append(x)
    ponto.append(y)
    if (x <= 0 and y + x*x + 2*x - 3 <= 0) or (x >= 0 and y + y + x*x - 2*x - 3 <= 0):
        print ("O ponto", ponto, "pertence a H.")
        freq += 1
    else:
        print ("O ponto", ponto, "não pertence a H.")
    print ("A frequência de pontos em H é", freq)
        
