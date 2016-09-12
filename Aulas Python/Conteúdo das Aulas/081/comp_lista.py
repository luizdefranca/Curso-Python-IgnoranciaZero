#compressão de lista = forma de gerar uma lista
#list comprehension

#formato geral:
#l = [x + 10 for x in range(10)]

#x + 10 --> expressão
#for x in range(10) --> for loop
#range(10) --> objeto iterável

#####- Mais rápidos que alguns for loops
#####- Sintaxe simples
#####- Velocidade de C

#a = open('ex.py')
#l = a.readlines()
#l = [linha.rstrip() for linha in l]

#l = [linha.rstrip() for linha in open('ex.py')]

#Eficiente em memoria e processamento


##### CLAUSULA IF #####

#logo depois do for loop

#import random
#l = [random.randint(1,100) for i in range(30)]
#l = [x for x in l if x%2==0]


##### NESTED FOR LOOP #####

#logo depois do for loop

#l = [x + y + z for x in 'abc' for y in 'lmn' for z in 'xyz']

print(l)
