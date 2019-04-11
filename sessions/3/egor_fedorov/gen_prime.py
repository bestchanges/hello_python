import math
import time


def primes():
    global sqrt_operations
    primes = []
    candidate = 1
    while True:
        candidate += 1
        is_prime = True
        search_till = math.sqrt(candidate)
        sqrt_operations += 1
        for prime in primes:
            if candidate % prime == 0:
                is_prime = False
                break
            if prime > search_till:
                break
        if not is_prime:
            continue
        primes.append(candidate)
        yield candidate


def primes_optimized():
    global sqr_operations
    sqr_operations = 0
    primes = [1]
    candidate = 1
    search_till_index = -1
    search_till_sqr = 0
    while True:
        candidate += 1
        if candidate > search_till_sqr:
            search_till_index += 1
            search_till_sqr = primes[search_till_index] ** 2
            sqr_operations += 1
            #print(f'{candidate} search till {primes[search_till_index]} (for max of {search_till_sqr})')

        is_prime = True
        for index in range(1, search_till_index + 1):
            prime = primes[index]
            if candidate % prime == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        primes.append(candidate)
        yield candidate


def next_n(g, n):
    val = None
    for i in range(n):
        val = next(g)
    return val


sqrt_operations = 0
sqr_operations = 0
num_of_primes = 100000
for gen in (primes(), primes_optimized()):
    start = time.time()
    last_prime = next_n(gen, num_of_primes)
    end = time.time()
    print(f"It took {int(end - start)} sec to find first {num_of_primes} of primes by {gen}. And it's value {last_prime}")
print(f'Number of sqr operations: {sqr_operations}')
print(f'Number of sqrt operations: {sqrt_operations}')