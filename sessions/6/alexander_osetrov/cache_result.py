from time import time
from math import factorial
from functools import wraps
from collections.abc import Hashable


class CacheResult:

    def __init__(self, func):
        self.func = func
        self.__name__ = self.func.__name__
        self.cache = {}

    def __call__(self, *args):
        if not isinstance(*args, Hashable):
            return self.func(*args)
        if args in self.cache:
            return self.cache[args]
        else:
            self.cache[args] = self.func(*args)
            return self.cache[args]

    def get_cache(self):
        return self.cache


def execution_time(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        started = time()
        result = func(*args, **kwargs)
        completed = time()
        print(f"Execution time for '{func.__name__}': {(completed - started)*1000} ms")
        return result
    return wrapped


@execution_time
@CacheResult
def test_cache_result(number):
    return factorial(number)


test_cache_result(10000)
test_cache_result(10000)
