import asyncio
import time
import requests


images = ['https://w7.pngwing.com/pngs/513/814/png-transparent-download-file-document-file-type-file-format-files-and-folders-icon.png',
'https://www.pngmart.com/files/1/Light-Bulb-PNG-Free-Download.png']


async def download(some_url):
    response = requests.get(some_url)
    filename = some_url.split('/')[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Картинка скачана за {time.time() - start_time:.2f} сек")


start_time = time.time()

processes = []

if __name__ == '__main__':
    tasks = []

    for img in images:
        task = asyncio.ensure_future(download(img))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))