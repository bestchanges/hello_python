import time


def time_decorator(source_function):
    def wrapper(*args, **kwargs):
        started = time.time()
        source_function(*args, **kwargs)
        finished = time.time()
        print(finished - started)
    return wrapper


@time_decorator
def some(t):
    print("some")
    time.sleep(t)


some(0.2)