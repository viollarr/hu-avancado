from threading import Thread
from time import sleep, time

def count_list(name, n, list_count):
    sleep(1)
    for i in range(n):
        list_count.append({'nome':name, 'numero': i})

    return list_count


if __name__ == '__main__':
    print('inicio')
    n = 10
    n_processos = 2
    elapsed = time()
    minha_list = []
    serial_elapsed = time() - elapsed
    processos = [
        Thread(target=count_list, args=[f'Processo {i}:', n, minha_list])
        for i in range(n_processos)
    ]

    elapsed = time()
    for p in processos:
        p.start()
    for p in processos:
        p.join()

    for til in minha_list:
        print(til)

    print('Fim')
