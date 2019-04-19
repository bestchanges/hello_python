def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def generate_next_prime(start_number):
    while True:
        if is_prime(start_number):
            yield start_number
        start_number += 1


primes = set()
for next_prime in generate_next_prime(0):
    if next_prime < 100:
        primes.add(next_prime)
    else:
        break
print(f'Primes: {primes}')

primeGenerator = generate_next_prime(0)
firstPrime = next(primeGenerator)
secondPrime = next(primeGenerator)
thirdPrime = next(primeGenerator)
print(f'Single prime values: {firstPrime}, {secondPrime}, {thirdPrime}')

input('Press any key for infinite generation')
while True:
    print(next(primeGenerator))
