"""
Construa o seu próprio objeto
range
"""

#TESTES
testes = [(5,), (1.7,), ("opa",), (), (1,5,0), (1,5), (5,2), (5,2,-1)]

for t in testes:
    print("Teste: FOR I IN RANGE%s"%str(t))
    
    try:
        print("Resultados da iteração:", end = " ")
        for i in meu_range(*t):
            print(i, end = " ")

        print("\nObjeto range: %s"%meu_range(*t))

        print("Iterador: %s"%iter(meu_range(*t)))
    
    except (TypeError, ValueError) as e:
        print(e)

    print()
