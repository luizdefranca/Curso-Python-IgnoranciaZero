
try:
    x = int(input('Digite um numero: '))
except:
    print('Deu erro!')
    x = 0
finally:
    print(x)
