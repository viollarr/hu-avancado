""""
>>> dict(contagem('banana').items())
{'b': 1, 'a': 3, 'n': 2}
>>> dict(contagem('maça').items())
{'m': 1, 'a': 2, 'ç': 1}
"""
from time import time
from bisect import bisect_right
from collections import Counter

def contagem(caracteres):
    return Counter(caracteres)


if __name__ == '__main__':
    elapsed = time()
    print(contagem('banana'))
    print(f'Total time: {time()-elapsed}s')

    elapsed = time()
    lst = [1, 1] + list(range(2, 100))
    print(bisect_right(lst, 1))
    print(f'Total time: {time()-elapsed}s')
