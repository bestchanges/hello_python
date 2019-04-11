import time
from typing import Iterable


def happy_tickets(start_from=0):
    v = start_from
    while True:
        if v >= 1000000:
            return
        digits = [v % 10 ** x // 10 ** (x - 1) for x in range(6, 0, -1)]
        assert len(digits) == 6
        if sum(digits[0:3]) == sum(digits[-3:]):
            yield ''.join([str(i) for i in digits])
        v += 1


pows_of_ten = [10 ** x for x in range(0, 7)]


def happy_tickets_optimized(start_from=0):
    v = start_from
    while True:
        if v >= 1000000:
            return
        digits = [v % pows_of_ten[x] // pows_of_ten[x - 1] for x in range(6, 0, -1)]
        assert len(digits) == 6
        if sum(digits[0:3]) == sum(digits[-3:]):
            yield ''.join([str(i) for i in digits])
        v += 1


def happy_tickets_str(start_from=0):
    v = start_from
    while True:
        if v >= 1000000:
            return
        s = f'{v:06}'
        digits = [int(digit) for digit in s]
        assert len(digits) == 6
        if sum(digits[0:3]) == sum(digits[-3:]):
            yield s
        v += 1


def exhaust_iterator(iter: Iterable):
    counter = 0
    start = time.time()
    for item in iter:
        counter += 1
    finish = time.time()
    return counter, finish - start


for iter in [happy_tickets, happy_tickets_optimized, happy_tickets_str]:
    value, runtime = exhaust_iterator(happy_tickets_optimized())
    print(f"Found {value} time: {runtime:.2} Iter: {iter}")
