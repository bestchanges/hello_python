import time
from threading import Thread
from threading import Semaphore


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
        print(f'Philosopher {self.name} is thinking...\n', end='')
        time.sleep(1)

    def take_fork(self, i):
        print(f'Philosopher {self.name} wants to take fork {i}\n', end='')
        while not forks.acquire(blocking=False):
            print(f'Philosopher {self.name} has no forks available, waiting...\n', end='')
            time.sleep(1)
        else:
            print(f'Philosopher {self.name} took fork {i}\n', end='')

    def eat(self):
        print(f'Philosopher {self.name} is eating...\n', end='')
        time.sleep(1)

    def put_fork(self, i):
        print(f'Philosopher {self.name} is putting fork {i}\n', end='')
        forks.release()

    def run(self):
        while True:
            self.think()
            self.take_fork(self.index)
            self.take_fork((self.index + 1) % number_of_forks)
            self.eat()
            self.put_fork(self.index)
            self.put_fork((self.index + 1) % number_of_forks)


Philosopher(0, 'Plato')
Philosopher(1, 'Aristotle')
Philosopher(2, 'Socrates')
Philosopher(3, 'Kant')
Philosopher(4, 'Descartes')

while True:
    pass
