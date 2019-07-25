import time
from threading import Thread
from test_single_thread import COUNT, countdown

NUM_THREADS = 4

threads = [Thread(target=countdown, args=(COUNT//NUM_THREADS,)) for i in range(NUM_THREADS)]

start = time.time()

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end = time.time()

print('Time taken in seconds -', end - start)