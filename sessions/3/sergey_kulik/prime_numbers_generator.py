import time


def get_primes():
    i = 0
    counter = 1
    while True:
        if i > 1:
            for x in range(2, i):
                if i % x == 0:
                    break
            else:
                counter += 1
                yield i
        i += 1


i = get_primes()
start = time.time()
for x in range(0, 1000):
    print(next(i))
end = time.time()
print("Calculation took ", end - start, ' seconds')
