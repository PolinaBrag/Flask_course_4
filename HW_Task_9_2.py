from multiprocessing import Process
import time
import requests


images = ['https://w7.pngwing.com/pngs/513/814/png-transparent-download-file-document-file-type-file-format-files-and-folders-icon.png',
'https://www.pngmart.com/files/1/Light-Bulb-PNG-Free-Download.png']


def download(some_url):
    response = requests.get(some_url)
    filename = some_url.split('/')[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Картинка скачана за {time.time() - start_time:.2f} сек")


start_time = time.time()

processes = []

if __name__ == '__main__':
    for img in images:
        p = Process(target=download, args=(img,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
