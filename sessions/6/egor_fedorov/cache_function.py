import time


def cache_result(target_function):
    cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        try:
            if not key in cache:
                result = target_function(*args, **kwargs)
                cache[key] = result
            return cache[key]
        except TypeError:
            return target_function(*args, **kwargs)
    return wrapper


@cache_result
def expensive(s):
    time.sleep(2)
    return 'zzz ' + str(s)


print(expensive([]))
print(expensive(s='wake'))
print(expensive(s='wake'))
print(expensive('wake'))
print(expensive('wake'))
print(expensive(s='another wake'))
print(expensive(s='another wake'))
