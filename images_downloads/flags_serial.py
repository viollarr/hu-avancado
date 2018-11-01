import string
from itertools import product
from os import path
from time import time
import requests

class FlagNotFound(Exception):
    pass

flags_dir = path.dirname(__file__)
flags_dir = path.join(flags_dir, 'images')


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


def download_all_flags():
    for country in generate_countries():
        try:
            image = download_flag(country)
        except FlagNotFound:
            yield f'Flag not found: {country}'
        else:
            path = save_flag(image, country)
            yield path


if __name__ == '__main__':

    elapsed = time()
    for result in download_all_flags():
        print(result)
    print(f'Total time: {time()-elapsed}s')
