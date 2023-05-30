import random
from multiprocessing import Process
import time


my_arr = [random.randint(0, 100) for i in range(1_000_000 + 1)]


def count_sum(arr):
    sum_arr = 0
    for i in arr:
        sum_arr += i
    print(sum_arr)
    print(f"Сумма почситана за  {time.time() - start_time:.2f} сек")


start_time = time.time()


processes = []


if __name__ == '__main__':
    for i in range(5):
        p = Process(target=count_sum, args=(my_arr,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

