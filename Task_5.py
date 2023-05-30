from multiprocessing import Process

files = ['test.txt', 'test2.txt', 'test3.txt']


def counter_word(some_file):
    with open(some_file, "r", encoding='utf-8') as f:
        content = f.read()
        count_words = len(content.split())
    print(f'Количество слов в файле {count_words}')


processes = []


if __name__ == '__main__':
    for file in files:
        p = Process(target=counter_word, args=(file,))
        processes.append(p)
        p.start()
        print('Процесс начал')

    for process in processes:
        process.join()
        print('Процесс закончил')
