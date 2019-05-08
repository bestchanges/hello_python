import time
import math


def is_prime_v1(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_v2(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def generate_next_prime_v1(start_number):
    while True:
        if is_prime_v1(start_number):
            yield start_number
        start_number += 1


def generate_next_prime_v2(start_number):
    while True:
        if is_prime_v2(start_number):
            yield start_number
        start_number += 1


def generate_100000_primes_v1():
    print('Primes generator v1 started')
    primes = set()
    start = time.time()
    for next_prime in generate_next_prime_v1(0):
        primes.add(next_prime)
        if next_prime >= 10000:
            break
    end = time.time()
    print(f'Primes: {primes}')
    print(f'Time taken: {end - start}')


def generate_100000_primes_v2():
    print('Primes generator v2 started')
    primes = set()
    start = time.time()
    for next_prime in generate_next_prime_v2(0):
        if next_prime < 100000:
            primes.add(next_prime)
        else:
            break
    end = time.time()
    print(f'Primes: {primes}')
    print(f'Time taken: {end - start}')


generate_100000_primes_v1()
generate_100000_primes_v2()
primeGenerator = generate_next_prime_v1(0)
firstPrime = next(primeGenerator)
secondPrime = next(primeGenerator)
thirdPrime = next(primeGenerator)
print(f'Single prime values as an example of calling next: {firstPrime}, {secondPrime}, {thirdPrime}')

input('Press any key for infinite generation')
while True:
    print(next(primeGenerator))
