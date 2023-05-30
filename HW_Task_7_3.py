import random
import asyncio
import time


my_arr = [random.randint(0, 100) for i in range(1_000_000 + 1)]


async def count_sum(arr):
    sum_arr = 0
    for i in arr:
        sum_arr += i
    print(sum_arr)
    print(f"Сумма почситана за  {time.time() - start_time:.2f} сек")


start_time = time.time()

if __name__ == '__main__':
    tasks = []

    for i in range(5):
        task = asyncio.ensure_future(count_sum(my_arr))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
