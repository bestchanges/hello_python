import random as rnd
import sys


def is_prime(number):
    simple_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if number < 100:
        if number in simple_primes:
            return True
        else:
            return False
    else:
        for p in simple_primes:
            if number % p == 0:
                return False
        i = 99
        while i * i < number:
            if number % i == 0:
                return False
            i += 2
        return True


num = rnd.randint(2, sys.maxsize)
if num % 2 == 0 and not is_prime(num):
    num += 1
while not is_prime(num):
    num += 2
print(f"Prime number generated {num}")
