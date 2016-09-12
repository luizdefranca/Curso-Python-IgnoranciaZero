def main ():
    gab = []
    cartao(gab)
    n = int(input("Digite o número de alunos: "))
    for j in range (n):
        lista = []
        cartao(lista)
        comp (lista, gab)
        print("O aluno %d teve %d acertos."%(j+1,acerto))

def cartao(lista):
    for i in range (30):
        q = input("Digite a resposta %d de 30: "%(i+1))
        lista.append(q)
    return lista

def comp (lista, gab):
    acerto = 0
    for i in range (30):
        if lista[i] == gab[1]:
            acerto += 1
    return acerto
main ()
