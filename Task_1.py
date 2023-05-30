import requests
import threading

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ]


def download(some_url):
    response = requests.get(some_url)
    filename = 'threading_' + some_url.replace('https://',
                                          '').replace('.', '_').replace('/', '') + '.html'
    with open(filename, "w", encoding='utf-8') as f:
        f.write(response.text)


threads = []

for url in urls:
    t = threading.Thread(target=download, args=[url])
    threads.append(t)
    t.start()
    print('Процесс начал')

for thread in threads:
    thread.join()
    print('Процесс закончил')
