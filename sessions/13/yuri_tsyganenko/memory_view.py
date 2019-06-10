#!/usr/bin/env python3
#  taken at  https://stackoverflow.com/questions/18655648/what-exactly-is-the-point-of-memoryview-in-python#34257357

import time
for n in (100000, 200000, 300000, 400000):
    data = 'x'*n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    print('bytes {:d} {:f}'.format(n, time.time()-start))

for n in (100000, 200000, 300000, 400000):
    data = b'x'*n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    print('memoryview {:d} {:f}'.format(n, time.time()-start))
