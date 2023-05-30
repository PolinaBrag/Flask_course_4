import random
import threading
import time


my_arr = [random.randint(0, 100) for i in range(1_000_000 + 1)]


def count_sum(arr):
    sum_arr = 0
    for i in arr:
        sum_arr += i
    print(sum_arr)
    print(f"Сумма поcчитана за  {time.time() - start_time:.2f} сек")


start_time = time.time()


threads = []

for i in range(5):
    t = threading.Thread(target=count_sum, args=(my_arr, ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
