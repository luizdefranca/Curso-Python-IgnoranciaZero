x = float(input("Digite o capital inicial: "))
z = float(input("Digite os juros mensais: "))
for t in range (12):
    c = x*((1 + (z/100))**(t + 1))
    print ("O montante do mês %d foi %.2f" %(t+1,c))
