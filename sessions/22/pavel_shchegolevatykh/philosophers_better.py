# solution using states and monitor to allow maximum degree of parallelism


import time
import logging
from enum import Enum
from threading import Thread
from threading import Semaphore

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

log_stream_handler = logging.StreamHandler()
log_stream_handler.setFormatter(log_formatter)

logger.addHandler(log_stream_handler)


class State(Enum):
    THINKING = 0
    HUNGRY = 1
    EATING = 2


number_of_philosophers = 5
forks = Semaphore(number_of_philosophers)

mutex = Semaphore(1)

state = [State.THINKING for i in range(number_of_philosophers)]


def left(index):
    return (index + number_of_philosophers - 1) % number_of_philosophers


def right(index):
    return (index + 1) % number_of_philosophers


def test(index):
    if state[index] == State.HUNGRY and state[left(index)] != State.EATING and state[right(index) != State.EATING]:
        state[index] = State.EATING
        logger.info(f'Philosopher {index} takes fork {left(index)} and {index}\n')
        logger.info(f'Philosopher {index} is eating\n')
        forks.release()


def take_forks(index):
    mutex.acquire()
    state[index] = State.HUNGRY
    test(index)
    mutex.release()
    forks.acquire()


def put_forks(index):
    mutex.acquire()

    state[index] = State.THINKING
    logger.info(f'Philosopher {index} putting fork {left(index)} and {index} down\n')
    logger.info(f'Philosopher {index} is thinking\n')

    test(left(index))
    test(right(index))
    mutex.release()


def think(): time.sleep(1)


def eat(): time.sleep(1)


class Philosopher(Thread):
    def __init__(self, index):
        Thread.__init__(self)
        self.index = index
        self.daemon = True
        self.start()

    def run(self):
        while True:
            think()
            take_forks(self.index)
            eat()
            put_forks(self.index)


Philosopher(0)
Philosopher(1)
Philosopher(2)
Philosopher(3)
Philosopher(4)

while True:
    pass
