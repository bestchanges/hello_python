# naive (wrong) solution
# deadlock is possible on circular wait for each fork
# if everyone picks up left fork first - everyone succeeds
# if everyone picks up right fork first - deadlock
# deadlock output example can be found in deadlock.log


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
            self.take_fork(self.index)
            self.take_fork((self.index + 1) % number_of_forks)
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
