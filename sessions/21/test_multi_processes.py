import time
from multiprocessing.pool import Pool
from test_single_thread import COUNT, countdown

NUM_PROCESSES = 4

start = time.time()

pool = Pool(processes=NUM_PROCESSES)
start = time.time()

for process in range(NUM_PROCESSES):
    pool.apply_async(countdown, [COUNT // NUM_PROCESSES])

pool.close()
pool.join()

end = time.time()
print('Time taken in seconds -', end - start)

