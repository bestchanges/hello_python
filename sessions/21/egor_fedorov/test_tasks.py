"""
The goal is to test different tasks for GIL limitations.
"""
import time
from multiprocessing.pool import Pool
from threading import Thread

from tasks import file_io, sleep, decrement, product, network_io
import logging

logging.basicConfig(
    format='%(message)s',
    datefmt="%H:%M:%S",
    level=logging.INFO
)

def measure(runner_function, task_function, runner_kwargs=None):
    start_at = time.time()
    runner_function(task_function, **runner_kwargs if runner_kwargs else {})
    finished_at = time.time()
    logging.info(f'For "{task_function.__name__}"  it takes {finished_at - start_at:.4f} runned with {runner_function.__name__}({runner_kwargs})')


def run_single_thread(task_function):
    task_function()


def run_multiple_threads(task_function, num_threads):
    threads = [Thread(target=task_function, kwargs={'divided_by': num_threads}) for i in range(num_threads)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def run_multiple_processes(task_function, num_processes):
    pool = Pool(processes=num_processes)

    for process in range(num_processes):
        pool.apply_async(task_function, kwds= {'divided_by': num_processes})

    pool.close()
    pool.join()


for task_function in file_io, sleep, decrement, product, network_io:
    # run single
    measure(run_single_thread, task_function)
    # run with threads
    measure(run_multiple_threads, task_function, runner_kwargs={'num_threads': 4})
    # run with processess
    measure(run_multiple_processes, task_function, runner_kwargs={'num_processes': 4})
