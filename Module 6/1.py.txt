import time
from threading import Thread

def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)

t1 = time.time()

threads = [Thread(target=get_thread, args=("Поток " + str(i+1), )) for i in range(5)]
for t in threads:
    t.start()

for t in threads:
    t.join()

print("Время работы программы с потоками:", round(time.time() - t1, 2), "секунд")

t2 = time.time()

for i in range(5):
    get_thread("Thread " + str(i+1))
    print("Время работы программы последовательно:", round(time.time() - t2, 2), "секунд")
