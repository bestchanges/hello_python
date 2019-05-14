from time import time


def prime_numbers(limit):
    """straightforward, but taking into account that divisor cannot be greater than square root of n"""
    primes = [2, 3, 5]
    for p in primes:
        yield p
    n = 5
    count = 3
    last_idx = -1
    sqrd_prime = 0
    while count <= limit:
        n += 2
        if n > sqrd_prime:
            last_idx += 1
            sqrd_prime = primes[last_idx] ** 2
        is_prime = True
        for i in range(1, last_idx + 1):
            p = primes[i]
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            primes.append(n)
            yield n


start = time()
g = prime_numbers(300000)
for i in range(300000):
    val = next(g)
print(val)
end = time()
print("time consumed: ", round(end - start, 3))
