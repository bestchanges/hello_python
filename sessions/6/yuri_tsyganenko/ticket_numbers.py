"""
Counting happy tickets with tracking time it takes to count them
"""

from functools import wraps
import time



def my_logger(func):
    import logging
    logging.basicConfig(filename='test_timing.log', level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Ran {} with args: {}, and kwargs: {}'.format(func.__name__, args, kwargs))
        #print('Ran {} with args: {}, and kwargs: {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return wrapper


def timer(func):
    @wraps(func)
    def wrapper_for_timering(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print("{} took {}".format(func.__name__, end_time - start_time))
        return value
    return wrapper_for_timering


# uncomment the @timer decorator below to get runtime error: line 53, in count_good_numbers
#     for i in goodNumbers():
# TypeError: 'NoneType' object is not iterable
#
#
#@my_logger
@timer
def goodNumbers():
    sums = {s: [] for s in range(0, 28)}  # Initially empty list for each sum

    for i1 in range(10):
        for i2 in range(10):
            for i3 in range(10):
                sums[i1 + i2 + i3].append((i1, i2, i3))

    time.sleep(4)  # DEBUG - Identify why decorator output is before this delay?
    for s in range(0, 28):
        for left in sums[s]:
            for right in sums[s]:
                yield "{}{}{}{}{}{}".format(left[0], left[1], left[2], right[0], right[1], right[2])


#@timer
def count_good_numbers():
    cnt = 0
    for i in goodNumbers():
        cnt += 1
    return cnt

print(count_good_numbers())

