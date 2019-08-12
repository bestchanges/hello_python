import time

COUNT = 10_000_000

def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    start = time.time()
    countdown(COUNT)
    end = time.time()
    print('Time taken in seconds -', end - start)