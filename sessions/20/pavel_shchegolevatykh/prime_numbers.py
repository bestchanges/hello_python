import time
import math
import argparse


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


def generate_next_prime(start_number, compare_func):
    while True:
        if compare_func(start_number):
            yield start_number
        start_number += 1


def generate_primes(compare_func, max_number):
    print(f'Primes generator {compare_func.__name__} started')
    primes = set()
    start = time.time()
    for next_prime in generate_next_prime(0, compare_func):
        primes.add(next_prime)
        if next_prime >= max_number:
            break
    end = time.time()
    print(f'Primes: {primes}')
    print(f'Time taken: {end - start}')


def main():
    parser = argparse.ArgumentParser(description='Selecting version of prime number generator')
    parser.add_argument('-v', '--version', metavar='', type=int,
                        help='Specifies compare func version 1 - means slow naive, 2 - faster optimized.')
    parser.add_argument('--max', required=True, metavar='', type=int,
                        help='Specifies max number that we generate primes until')
    args = parser.parse_args()

    generate_primes(is_prime_v1, args.max) if args.version == 1 else generate_primes(is_prime_v2, args.max)
    prime_generator = generate_next_prime(0, is_prime_v1 if args.version == 1 else is_prime_v2)
    first_prime = next(prime_generator)
    second_prime = next(prime_generator)
    third_prime = next(prime_generator)
    print(f'Single prime values as an example of calling next: {first_prime}, {second_prime}, {third_prime}')

    input('Press any key for infinite generation')
    while True:
        print(next(prime_generator))


if __name__ == '__main__':
    main()
