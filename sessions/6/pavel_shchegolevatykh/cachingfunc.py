import time
from functools import wraps


def cache(function):
    cache = {}
    @wraps(function)
    def wrapper(*args, **kwargs):
        # for simplicity
        key = repr(args) + repr(kwargs)
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]
    return wrapper


@cache
def expensive(n):
    time.sleep(2)
    return f"Done for {n}"


start = time.time()
expensive(25)
end = time.time()
print(f'Time taken first time (fresh value): {end - start}')
start = time.time()
expensive(25)
end = time.time()
print(f'Time taken second time (cached value): {end - start}')
start = time.time()
expensive(3)
end = time.time()
print(f'Time taken third time (fresh value): {end - start}')
