"""
Reverse block by block in big string and compare time for regular string and with using memoryview
"""
import time
import random
import string


# create sample data
BLOCK_SIZE = 1024
BLOCK_NUM = 5000
data = ''
start = time.time()
for i in range(BLOCK_NUM):
    data += ''.join(random.choices(string.ascii_letters + string.digits, k=BLOCK_SIZE))
print(f'create dummy data - {time.time() - start:.3f}s')

# regular string
start = time.time()
new_data = ''
for i in range(BLOCK_NUM):
    block = data[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE]
    block = block[::-1]
    new_data += block
str_elapsed = time.time() - start
print(f'time elapsed for string {str_elapsed:.3f}s')

# using memoryview
start = time.time()
mv = memoryview(bytearray(data, 'ascii'))
for i in range(BLOCK_NUM):
    block = mv[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE]
    block = block[::-1]
    mv[i*BLOCK_SIZE : (i+1)*BLOCK_SIZE] = block
data = mv.tobytes().decode('ascii')
mv_elapsed = time.time() - start
print(f'time elapsed for memoryview {mv_elapsed:.3f}s')

print(f'memoryview is {str_elapsed/mv_elapsed:.1f}x faster')
