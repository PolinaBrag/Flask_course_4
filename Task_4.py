import requests
import threading
import pathlib

files = ['test.txt', 'test2.txt', 'test3.txt']


def counter_word(some_file):
    with open(some_file, "r", encoding='utf-8') as f:
        content = f.read()
        count_words = len(content.split())
    print(f'Количество слов в файле {count_words}')


threads = []

for file in files:
    t = threading.Thread(target=counter_word, args=[file])
    threads.append(t)
    t.start()
    print('Процесс начал')

for thread in threads:
    thread.join()
    print('Процесс закончил')

