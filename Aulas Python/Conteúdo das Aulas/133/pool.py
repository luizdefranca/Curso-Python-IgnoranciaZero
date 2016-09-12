import multiprocessing

def faz_calculo(dado):
    return dado * 2

def inicia_processo():
    print('Iniciando', multiprocessing.current_process().name)

if __name__ == '__main__':
    inputs = list(range(10))
    print('Input   :', inputs)
    
    builtin_outputs = map(faz_calculo, inputs)
    print('Built-in:', builtin_outputs)
    
    pool_tam = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_tam,
                                initializer=inicia_processo,
                                )
    pool_outputs = pool.map(faz_calculo, inputs)
    pool.close()
    pool.join()

    print('Pool    :', pool_outputs)
