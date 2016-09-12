#Map
#--> Recebe uma expressão e um objeto iterável
#    e se comporta como um compressão de lista
#    percorrendo cada elemento do objeto e
#    aplicando a expressão neste gerando
#    um novo objeto map
#list(map(ord, 'abcde'))

#--> É mais rápido do que for loops, porem
#    mais lento do que compressão de listas
#l1 = [1,2,3,4]
#l = [x**2 for x in l1]
#ou
#l = list(map(lambda x: x**2, l1))

#l = [x for x in l1 if x%2 == 0]
#ou
#l = list(map(lambda x: x%2 == 0, l1))

