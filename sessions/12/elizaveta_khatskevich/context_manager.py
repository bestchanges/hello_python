from contextlib import contextmanager
import time
import requests


class RequestTimingClass:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exception, value, traceback, *args):
        self.end = time.time()
        print(value) if value else None
        print(f"Fetching {self.name} took {self.end - self.start:.2f}")
        return True


@contextmanager
def request_timing(name):
    start = time.time()
    try:
        yield name
    except requests.exceptions.ConnectionError:
        print(f"Page {name} not found")
    finally:
        end = time.time()
        print(f"Fetching {name} took {end - start:.2f}")


def main_function():
    with request_timing('http://arnavk.com/posts/python-context-managers/') as domain_name:
        conn = requests.get(f'https://{domain_name}')
        print(conn.status_code)
        conn.close()
    with RequestTimingClass('google.com'):
        conn = requests.get(f"https://google.com")
        print(conn.status_code)


if __name__ == "__main__":
    main_function()
