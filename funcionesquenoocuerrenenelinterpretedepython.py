from time import sleep, time
from threading import Thread
start = time()
for _ in range(10):
    sleep(1)
print('Tomó {} segundos.'.format(time() - start))


threads = []
start = time()
for _ in range(10):
    t = Thread(target=sleep, args=(1,))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
print('Tomó {} segundos.'.format(time() - start))
