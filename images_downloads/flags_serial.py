import string
from itertools import product
from os import path
from time import time
import requests

class FlagNotFound(Exception):
    pass

flags_dir = path.dirname(__file__)
flags_dir = path.join(flags_dir, 'images')


def get_url(uf, port):
    url = 'http://localhost:{}/flags'.format(port)
    return '{0}/{1}/{1}.gif'.format(url, uf)

def download_flag(country, port):
    url = get_url(country, port)
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


def download_all_flags(port):
    for country in generate_countries():
        try:
            image = download_flag(country, port)
        except FlagNotFound:
            yield f'Flag not found: {country}'
        else:
            path = save_flag(image, country)
            yield path


if __name__ == '__main__':

    elapsed = time()
    for result in download_all_flags(8001):
        print(result)
    print(f'Total time: {time()-elapsed}s')
