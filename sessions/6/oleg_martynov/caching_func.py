import time
import json

def cached(fn):

    cache = {}
    def wrapped_fn(*args, **kwargs):
        nonlocal cache
        input_args = (args, tuple(kwargs.items()))
        if input_args in cache.keys():
            print("getting result from cache")
            return cache.get(input_args)
        else:
            print("no cache hit, evaluate function and cache the result")
            fn_result = fn(*args, **kwargs)
            cache[input_args] = fn_result
            return fn_result

    return wrapped_fn

#Some tests

@cached
def sum_fixed(a, b, c, d):
    time.sleep(10)
    return a+b+c+d
@cached
def sum_var(*args):
    time.sleep(10)
    return sum(args)

@cached
def jsonify_input(*args, **kwargs):
    time.sleep(10)
    return json.dumps([args, kwargs], indent=4)

print(sum_fixed(1,2,3,4))
print(sum_fixed(1,2,3,4))

print(sum_var(2,3,4,5,6,7,8,9))
print(sum_var(2,3,4,5,6,7,8,9))

print(jsonify_input("hey", "ho", "lets", "go", straight="line", tight="wind"))
print(jsonify_input("hey", "ho", "lets", "go", straight="line", tight="wind"))