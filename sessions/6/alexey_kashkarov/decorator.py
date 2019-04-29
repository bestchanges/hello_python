import functools
import time


cache = dict()


def cache_result(func):
    """Saves the result of the decorated function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        else:
            result = func(*args, **kwargs)
            cache[args] = result
            return result
    return wrapper


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.8f} secs")
        return value
    return wrapper_timer


@cache_result
def gcd(a, b):
    """Calculates greatest common divisor"""
    while b > 0:
        a = a % b
        a, b = b, a
    return a


@timer
@cache_result
def lcm(a, b):
    """Calculates least common multiplier"""
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    a = 97454363
    b = 1853473
    # calculate lcm for nig numbers
    print(lcm(a, b))
    print(cache)
    # calculate again to get result from cache
    print(lcm(a, b))
