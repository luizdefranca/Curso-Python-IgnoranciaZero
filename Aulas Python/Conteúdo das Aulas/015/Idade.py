n = int(input("Digite o numero de pessoas: "))

cont = 0

while cont < n:

    dia = int(input("Digite o dia de nascimento da pessoa %i: "%(cont+1)))
    mes = int(input("Digite o mes de nascimento da pessoa %i: "%(cont+1)))
    ano = int(input("Digite o ano de nascimento da pessoa %i: "%(cont+1)))
    idade = int(input("Digite a idade a ser completada da pessoa %i: "%(cont+1)))

    print("A pessoa %i fara %i anos no dia %d/%i/%d" %(cont+1, idade, dia, mes, ano+idade))

    cont += 1

#Para inteiros --> %i ou %d
#Colocar % --> %%
