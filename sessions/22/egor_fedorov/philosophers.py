import logging
import random
from threading import Thread, Lock, RLock
from time import sleep
from typing import Optional

logging.basicConfig(
    format='%(relativeCreated)6d %(threadName)15s: %(message)s',
    level=logging.DEBUG,
)

dinner_is_over = False


class StateError(Exception): pass


class Fork:
    def __init__(self, number: int):
        super().__init__()
        self.number = number
        self.taken = None
        self.lock = RLock()

    def __str__(self):
        return f'Fork({self.number})'

    def take_by(self, philosopher):
        if not self.lock.acquire(blocking=False):
            raise StateError("Already aquired")
        if self.taken:
            raise StateError()
            # raise RuntimeError("Shall not happened as soon as lock acquired")
        self.taken = philosopher
        return True

    def put_back(self, philisopher: 'Philosopher'):
        if not self.taken:
            raise StateError("Not taken")
        if not self.taken == philisopher:
            raise StateError(f"It's taken by {self.taken}")
        self.lock.release()
        self.taken = None
        return True


class Philosopher(Thread):
    def __init__(self, name: str, fork_left: Fork = None, fork_right: Fork = None, max_eat_time=1) -> None:
        super().__init__(name=name)
        self.eat_times = 0
        self.max_eat_time = max_eat_time
        self.is_hungry = True
        if fork_right and fork_left:
            self.my_forks(fork_left, fork_right)

    def my_forks(self, fork_left: Optional[Fork], fork_right: Optional[Fork]):
        # sort forks to use ordering restriction while acquiring locks
        self.forks = sorted((fork_left, fork_right), key=lambda fork: fork.number)
        # TODO: strange using same-ordered forks does work as well
        # self.forks = (fork_left, fork_right)

    def run(self):
        while not dinner_is_over:
            try:
                self.eat()
            except StateError:
                logging.info(f"Cannot eat")
                self._put_forks()
            self.think()

    def __str__(self):
        return self.name

    def think(self):
        think_time = self.max_eat_time * random.random() / 2
        logging.debug(f"Thinkning for {think_time:.2f} seconds")
        sleep(think_time)

    def eat(self):
        logging.debug("Try to take forks")
        self._take_forks()
        eat_time = self.max_eat_time * random.random()
        logging.info(f"Start eating for {eat_time:.2f} seconds")
        sleep(eat_time)
        logging.info("End eating")
        self.eat_times += 1
        self._put_forks()

    def _take_forks(self):
        for fork in self.forks:
            fork.take_by(self)

    def _put_forks(self):
        # TODO: strange using non-reversed lock releases works as well
        for fork in reversed(self.forks):
            if fork.taken == self:
                fork.put_back(self)


PHILOSOPHER_NAMES = ('Socrates', 'Plato', 'Aristotle', 'Kant', 'Confucius')


def create_philosophers(names=PHILOSOPHER_NAMES):
    forks = [Fork(number + 1) for number, name in enumerate(names)]
    philosophers = [Philosopher(name) for number, name in enumerate(names)]
    for number, philosopher in enumerate(philosophers):
        right_fork = forks[number]
        left_fork = forks[number - 1 if number > 0 else len(philosophers) - 1]
        philosopher.my_forks(left_fork, right_fork)
    return philosophers


if __name__ == '__main__':
    # philosophers = create_philosophers([str(i) for i in range(2)])
    philosophers = create_philosophers()
    for philosopher in philosophers:
        philosopher.start()
    sleep(5)
    dinner_is_over = True
    for philosopher in philosophers:
        philosopher.join()
    for philosopher in philosophers:
        logging.info(f"{philosopher} ate {philosopher.eat_times} times")
