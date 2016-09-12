while True:
    try:
        maximo = input()
    except EOFError:
        print(ult_max)
        break
    ult_max = maximo
