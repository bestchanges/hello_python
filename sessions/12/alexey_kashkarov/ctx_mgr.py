from datetime import datetime
import sys
import functools
from contextlib import contextmanager


def time_print(*args):
    """Custom print function"""
    sys.stdout.write(f'[{datetime.now()}] - {args[0]}\n')


class ExtendedPrintManager:
    """
    Context manager for overriding builtin print function.
    """
    def __init__(self):
        self._print = __builtins__.print

    def __enter__(self):
        __builtins__.print = time_print

    def __exit__(self, exc_type, exc_val, exc_tb):
        __builtins__.print = self._print


def extended_print(func):
    """
    Decorator for overriding builting print function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        original_print = __builtins__.print
        __builtins__.print = time_print
        res = func(*args, **kwargs)
        __builtins__.print = original_print
        return res
    return wrapper


@extended_print
def decorated_print(text):
    """
    Using decorator with builtin print override
    """
    print(text)


@contextmanager
def decorated_print_2():
    original_print = __builtins__.print
    __builtins__.print = time_print
    try:
        yield
    finally:
        __builtins__.print = original_print


if __name__ == "__main__":
    print("Original builtin print function")
    with ExtendedPrintManager():
        print("Extended print function using class Context Manager")
    print("Back to original print")
    decorated_print("Extended print with decorator function")
    print("And back to original print again")
    with decorated_print_2():
        print("Extended print function using contextlib")
    print("And finally back to original print")

