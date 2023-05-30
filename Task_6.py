import asyncio

files = ['test.txt', 'test2.txt', 'test3.txt']


async def counter_word(some_file):
    with open(some_file, "r", encoding='utf-8') as f:
        content = f.read()
        count_words = len(content.split())
    print(f'Количество слов в файле {count_words}')


if __name__ == '__main__':
    tasks = []

    for file in files:
        task = asyncio.ensure_future(counter_word(file))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
