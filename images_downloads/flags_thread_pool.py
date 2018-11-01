import string
from itertools import product
from os import path
from time import time
import requests
from threading import Thread, current_thread

class FlagNotFound(Exception):
    pass

flags_dir = path.dirname(__file__)
flags_dir = path.join(flags_dir, 'flags_thread')


def get_url(uf):
    return '{0}/{1}/{1}.gif'.format('http://localhost:8001/flags', uf)

def download_flag(country):
    url = get_url(country)
    resp = requests.get(url)
    if resp.status_code != 200:
        raise FlagNotFound()
    return resp.content


def save_flag(image, country):
    flag_path = path.join(flags_dir, f'{country}.gif')
    with open(flag_path, 'wb') as f:
        f.write(image)
    return flag_path


def generate_countries():
    for a, b in product(string.ascii_lowercase, string.ascii_lowercase):
        yield a + b

def download_and_save(country):
    try:
        image = download_flag(country)
    except FlagNotFound:
        print(f'Flag not found: {country}')
    else:
        path = save_flag(image, country)
        print(path)

def download_all_flags():
    threads = [
        Thread(target=download_and_save, args=[country])
        for country in generate_countries()
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':

    elapsed = time()
    download_all_flags()
    print(f'Total time: {time()-elapsed}s')
