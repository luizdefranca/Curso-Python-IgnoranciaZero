n = int(input("Digite o grau de p(x): "))
p = []
for i in range (n+1):
    a = float(input("Digite o a%d: "%(i)))
    p.append(a)
r = float(input("Digite alfa: "))
q = []
cont = 0
for j in range (len(p) - 1, 0, -1):
    if j == len(p) - 1:
        q.append(p[j])
    else:
        e = r*q[cont - 1] + p[j]
        q.append(e)
    cont += 1
q2 = []
for i in range(len(q) - 1, -1, -1):
    q2.append(q[i])
print(q2)
