from flags_serial import get_url, save_flag, generate_countries
from time import time
import aiohttp
import asyncio


async def download(country, port):
    print('Começando a executar future')
    async with aiohttp.ClientSession() as session:
        resp = await session.get(get_url(country, port))
        if resp.status != 200:
            raise Exception('Flag {} not found'.format(country))
        flag_bytes = await resp.read()
        return save_flag(flag_bytes, country)

async def download_all_flags(port):
    features = [download(country, port) for country in generate_countries()]
    r = await asyncio.wait(features)

    print(r)
    return 'final'

if __name__ == '__main__':

    elapsed = time()
    feature = download_all_flags(8001)
    asyncio.run(feature)
    print(f'Total time: {time()-elapsed}s')
