import requests
from multiprocessing import Process, Pool

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def download(some_url):
    response = requests.get(some_url)
    filename = 'multiprocessing_' + some_url.replace('https://',
                                          '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)


processes = []


if __name__ == '__main__':
    for url in urls:
        p = Process(target=download, args=(url,))
        processes.append(p)
        p.start()
        print('Процесс начал')

    for process in processes:
        process.join()
        print('Процесс закончил')

