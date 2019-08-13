# circular wait condition never arises if we have GLOBAL ordering of resources in place
# NO PROCESS can request a resource lower than it is already holding
# e.g. in our case it  works fine if we always take lower fork first and then higher indexed fork
# UNTIL the last philosopher
# e.g. first one takes 0, 1, second  1, 2, third 2, 3 until we get to
# the last philosopher who takes 4 and wants 0 and not vice versa
# deadlock is possible because ordering is not the same

import time
import logging
from threading import Thread
from threading import Semaphore

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

log_stream_handler = logging.StreamHandler()
log_stream_handler.setFormatter(log_formatter)

logger.addHandler(log_stream_handler)


number_of_forks = 5
forks = Semaphore(number_of_forks)


class Philosopher(Thread):
    def __init__(self, index, name):
        Thread.__init__(self)
        self.name = name
        self.index = index
        self.daemon = True
        self.start()

    def think(self):
        logger.info(f'Philosopher {self.name} is thinking...\n')
        time.sleep(1)

    def take_fork(self, i):
        logger.info(f'Philosopher {self.name} wants to take fork {i}\n')
        while not forks.acquire(blocking=False):
            logger.info(f'Philosopher {self.name} has no forks available, waiting...\n')
            time.sleep(1)
        else:
            logger.info(f'Philosopher {self.name} took fork {i}\n')

    def eat(self):
        logger.info(f'Philosopher {self.name} is eating...\n')
        time.sleep(1)

    def put_fork(self, i):
        logger.info(f'Philosopher {self.name} is putting fork {i}\n')
        forks.release()

    def run(self):
        while True:
            self.think()
            # self.take_fork(self.index) - the original condition that was before
            # corrected condition we always take FIRST min fork between left and right
            self.take_fork(min(self.index, (self.index + 1) % number_of_forks))
            # self.take_fork((self.index + 1) % number_of_forks) - the original condition that was before
            # corrected condition we always take SECOND max fork between left and right
            self.take_fork(max(self.index, (self.index + 1) % number_of_forks))
            self.eat()
            self.put_fork((self.index + 1) % number_of_forks)
            self.put_fork(self.index)


Philosopher(0, '0 (Plato)')
Philosopher(1, '1 (Aristotle)')
Philosopher(2, '2 (Socrates)')
Philosopher(3, '3 (Kant)')
Philosopher(4, '4 (Descartes)')

while True:
    pass
