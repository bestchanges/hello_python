"""
Counting happy tickets with tracking time it takes to count them
"""


import time


def timer(func):
    def wrapper_for_timering(*args,  **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print("{} took {}".format(func.__name__, end_time - start_time))
    return wrapper_for_timering


def goodNumbers():
    sums = {}
    for s in range(0, 28):
        sums[s] = []

    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                sums[i1 + i2 + i3].append((i1, i2, i3))

    for s in range(0, 28):
        for left in sums[s]:
            for right in sums[s]:
                yield "{}{}{}{}{}{}".format(left[0], left[1], left[2], right[0], right[1], right[2])


@timer
def count_good_numbers():
    cnt = 0
    for i in goodNumbers():
        cnt += 1
    return cnt

count_good_numbers()

