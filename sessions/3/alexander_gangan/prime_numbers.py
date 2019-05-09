from time import time
import math


def yield_suitable_prime(primes_list, square_root):
    for prime in primes_list:
        if prime <= square_root:
            yield prime



def dumb_prime_numbers(limit):
    """absolutely straightforward.. goes too long for 100k primes"""
    primes = [2, 3]
    n = 3
    count = 1
    while count <= limit:
        n += 2
        prime = True
        for p in primes:
            if not n % p:
                prime = False
        if prime:
            count += 1
            primes.append(n)
    return primes


def slow_prime_numbers(limit):
    """straightforward, but taking into account that divisor cannot be greater than square root of n"""
    primes = [2, 3, 5]
    for p in primes:
        yield p
    n = 5
    count = 3
    while count <= limit:
        n += 2
        print(*yield_suitable_prime(primes[1:], math.sqrt(n)))
        for p in yield_suitable_prime(primes[1:], math.sqrt(n)):
            if n % p == 0:
                break
        else:
            count += 1
            primes.append(n)
            yield n


start = time()
print(*slow_prime_numbers(150))
end = time()
print("time consumed: ", round(end - start, 3))
