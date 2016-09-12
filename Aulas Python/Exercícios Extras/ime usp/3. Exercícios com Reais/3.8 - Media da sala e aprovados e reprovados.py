n = int(input("Digite n: "))
lista_m = []
aprov = 0
soma_t = 0.0
for i in range (n):
    soma = 0.0
    for p in range (3):
        nota = float(input("Digite a nota %d de 3 do aluno %d: "%(p+1, i+1)))
        soma += nota
        soma_t += nota
    media = soma/3
    lista_m.append(media)
    if media >= 5:
        aprov += 1
media_c = soma_t/(3*n)
print ("Medias:", lista_m, "Aprovados:", aprov, "Reprovados:", n - aprov, "Média da classe: %.1f", %(media_c))
