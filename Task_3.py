import asyncio
import aiohttp

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


async def download(some_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(some_url) as response:
            text = await response.text()
            filename = 'asyncio_' + some_url.replace('https://',
                                    '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)


if __name__ == '__main__':
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
