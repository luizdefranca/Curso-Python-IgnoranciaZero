while True:
    try:
        num = int(input("Digite um número entre 1 e 20: "))
    except ValueError:
        print('Digite apenas numeros')
    except:
        print('Entrada invalida')
    else:
        break

test = True

if not 1<=num<=20:
    test = False

assert test, num

if __debug__:
    if not test:
        raise AssertionError(num)

