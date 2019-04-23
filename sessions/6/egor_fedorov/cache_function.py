import time


def cache_result(target_function):
    cache = {}

    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))
        try:
            hash(cache_key)
        except TypeError:
            # cannot cache
            return target_function(*args, **kwargs)
        if not cache_key in cache:
                result = target_function(*args, **kwargs)
                cache[cache_key] = result
        return cache[cache_key]
    return wrapper


@cache_result
def expensive(s):
    time.sleep(2)
    return 'zzz ' + str(s)


print(expensive(s='wake'))
print(expensive(s='wake'))
print(expensive('wake'))
print(expensive('wake'))
print(expensive(s='another wake'))
print(expensive(s='another wake'))
print(expensive([]))
print(expensive([]))
