"""
37.	Uma academia deseja fazer um senso entre seus clientes para descobrir
o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve
fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o
usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve
ser informados os códigos e valores do clente mais alto, do mais baixo, do
mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

"""

código = int(input("Digite o seu código: "))
if código != 0:
    maior_peso = menor_peso = peso_total = float(input("Digite seu peso: "))
    maior_alt = menor_alt = alt_total = float(input("Digite sua altura: "))
    
    código = int(input("Digite o seu código: "))
    cont = 1

    while código != 0:
        cont += 1
        peso = float(input("Digite seu peso: "))
        alt = float(input("Digite sua altura: "))

        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

        if alt > maior_alt:
            maior_alt = alt
        if alt < menor_alt:
            menor_alt = alt

        peso_total += peso
        alt_total + alt
        
        código = int(input("Digite o seu código: "))

print("Maior peso: %g kg"%maior_peso)
print("Menor peso: %g kg"%menor_peso)
print("Média de pesos: %g kg"%(peso_total/cont))
print("Maior altura: %g m"%maior_alt)
print("Menor altura: %g m"%menor_alt)
print("Média de alturas: %g"%(alt_total/cont))
