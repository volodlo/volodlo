import requests
import time
from threading import Thread

def get_html(link):
	text = requests.get(link).text
	print(f'{link} Длина текста: {len(text)}')

links=['https://vk.com/', 'https://telegram.org/', 'https://greenwayglobal.com/', 'https://www.youtube.com/', 'https://www.google.com/']
threads = [Thread(target = get_html, args = (links[i], )) for i in range(5)]
time1 = time.time()
for t in threads:
	t.start()
	t.join()
print(f'Время последовательного выполнения: {time.time()-time1}\n')

threads = [Thread(target = get_html, args = (links[i], )) for i in range(5)]
time1 = time.time()
for t in threads:
	t.start()
for t in threads:
	t.join()
print(f'Время параллельного выполнения: {time.time()-time1}')
