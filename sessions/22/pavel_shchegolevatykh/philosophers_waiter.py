# solution using waiter (arbitrator) to limit taking forks if only one left
# that way deadlocks are prevented but less people can eat at the same time
# compared to monitor (philosophers_better) solution

import threading
import time
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

log_stream_handler = logging.StreamHandler()
log_stream_handler.setFormatter(log_formatter)

logger.addHandler(log_stream_handler)


class Waiter:
    def __init__(self, max_value):
        self.lock = threading.Semaphore(max_value)

    def up(self):
        self.lock.acquire()

    def down(self):
        self.lock.release()


class Fork:
    def __init__(self, number):
        self.number = number
        self.lock = threading.Semaphore(1)
        self.taken = False

    def take(self):
        self.lock.acquire()
        self.taken = True
        self.lock.release()

    def put(self):
        self.lock.acquire()
        self.taken = False
        self.lock.release()


class Philosopher(threading.Thread):
    def __init__(self, philosopher_id, left_fork, right_fork, waiter):
        threading.Thread.__init__(self)
        self.philosopher_id = philosopher_id
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.waiter = waiter

    def think(self):
        logger.info(f'Philosopher {self.philosopher_id} is thinking...')
        time.sleep(1)

    def eat(self):
        logger.info(f'Philosopher {self.philosopher_id} is eating...')
        time.sleep(1)

    def run(self):
        while True:
            self.think()
            self.waiter.down()
            logger.info(f'Philosopher {self.philosopher_id} calls waiter')
            self.left_fork.take()
            logger.info(f'Philosopher {self.philosopher_id} takes left fork')
            self.right_fork.take()
            logger.info(f'Philosopher {self.philosopher_id} takes right fork')
            self.eat()
            self.right_fork.put()
            logger.info(f'Philosopher {self.philosopher_id} put right fork')
            self.left_fork.put()
            logger.info(f'Philosopher {self.philosopher_id} put left fork')
            self.waiter.up()
            logger.info(f'Philosopher {self.philosopher_id} says good bye to waiter')


def main():
    number_of_philosophers = 5
    # waiter for deadlock avoidance (n-1 available)
    waiter = Waiter(number_of_philosophers-1)
    forks = [Fork(i) for i in range(number_of_philosophers)]
    philosophers = [Philosopher(i, forks[i], forks[(i+1) % number_of_philosophers], waiter) for i in range(number_of_philosophers)]

    for i in range(number_of_philosophers):
        philosophers[i].start()


if __name__ == '__main__':
    main()
