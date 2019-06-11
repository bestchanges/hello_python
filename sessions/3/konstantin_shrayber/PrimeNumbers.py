primes = [2, 3, 5, 7]

search_limit = int(input("Specify number until we search primes: "))

for candidate in range(9, search_limit+1, 2):
    for prime in primes:
        if candidate % prime == 0:
            break
    else:
        primes.append(candidate)

print(primes)