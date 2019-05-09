import math
import time

ITERATIONS_LIMIT = 100000


def gen_prime_number():
    current_prime = 1
    primes = []

    while True:
        current_prime += 1
        is_prime = True
        prime_sqrt = math.sqrt(current_prime)
        for prime in primes:
            if current_prime % prime == 0:
                is_prime = False
                break
            if prime > prime_sqrt:
                break

        if not is_prime:
            continue

        primes.append(current_prime)
        yield current_prime


def gen_prime_number_optimized():
    current_prime = 1
    primes = []

    while True:
        current_prime += 1
        is_prime = True
        if current_prime not in [2, 3, 4] and \
                (current_prime % 2 == 0 or current_prime % 3 == 0 or current_prime % 5 == 0):
            continue
        prime_sqrt = math.sqrt(current_prime)
        for prime in primes:
            if current_prime % prime == 0:
                is_prime = False
                break
            if prime > prime_sqrt:
                break

        if not is_prime:
            continue

        primes.append(current_prime)
        yield current_prime


def do_iterations(it, iteration_limit):
    for _ in range(iteration_limit):
        next(it)


if __name__ == '__main__':
    for prime_func in [gen_prime_number(), gen_prime_number_optimized()]:
        t = time.time()
        do_iterations(prime_func, ITERATIONS_LIMIT)
        print('Execution time - {:.3f} sec in {}'.format(time.time() - t, prime_func.__name__))
