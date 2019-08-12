import tempfile
import time

import requests


def file_io_tiny(**kwargs):
    kwargs['size'] = 1024
    kwargs['times'] = 1000
    file_io(**kwargs)


def file_io(divided_by=1, times=100, content=b'x', size=1024*1024):
    for i in range(times // divided_by):
        with tempfile.TemporaryFile() as fp:
            fp.write(content * size)
            fp.seek(0)
            fp.read()


def network_io(divided_by=1, times=12, url='http://google.com', delay=200):
    for i in range(times // divided_by):
        requests.get(f'http://slowwly.robertomurray.co.uk/delay/{delay}/url/{url}')


def sleep(divided_by=1, times=12, delay=0.1):
    for i in range(times // divided_by):
        time.sleep(delay)


def decrement(divided_by=1, times=10_000_000):
    c = 0
    for i in range(times // divided_by):
        c - 1


def product(divided_by=1, to=1_000_000):
    for i in range(1, to, divided_by):
        i ** 4
