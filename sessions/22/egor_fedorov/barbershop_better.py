import logging
import random
from queue import Queue, Full, Empty
from threading import Thread, Condition
from time import sleep
from typing import NamedTuple


class Config(NamedTuple):
    CLIENTS: int
    BARBERS: int
    CHAIRS: int


CONFIGS = (
    Config(CLIENTS=2, CHAIRS=5, BARBERS=1),
    Config(CLIENTS=5, CHAIRS=3, BARBERS=1),
    Config(CLIENTS=20, CHAIRS=5, BARBERS=3),
    # Config(CLIENTS=10_000, CHAIRS=200, BARBERS=300),
)

logging.basicConfig(
    format='%(relativeCreated)6d %(threadName)15s: %(message)s',
    # format='%(relativeCreated)6d %(name)20s (Thread: %(threadName)15s): %(message)s       [%(filename)s:%(lineno)s]',
    level=logging.DEBUG ,
)


class Barber(Thread):
    def __init__(self, name) -> None:
        super().__init__(name=name)

    def run(self):
        while True:
            try:
                client = queue.get(timeout=1) # type: Client
                logging.info(f'serving {client}')
                sleep(0.5)
                client.served = True
                logging.debug(f'finish serving {client}')
                with client.awaited:
                    client.awaited.notify()
            except Empty:
                logging.info(f"I've been sleeping for a while. And there are no any clients come")
                if is_closed:
                    logging.info("we're closed. I go home")
                    return


class Client(Thread):
    def __init__(self, name) -> None:
        super().__init__(name=name)
        self.served = False
        self.awaited = Condition()

    def run(self):
        while True:
            sleep_for = (random.random() + 0.3) * 1.5
            logging.debug(f'go for a walk for {sleep_for:.2f} seconds')
            # You can test with failing Client threads
            # if random.randint(1,6) == 2:
            #     raise ArithmeticError()
            sleep(sleep_for)
            try:
                queue.put(self, timeout=0.1)
                logging.info(f'start waiting in the queue (queue length={queue.qsize()} of {queue.maxsize})')
                with self.awaited:
                    self.awaited.wait()
                logging.debug(f'I has my hair cut! (queue length={queue.qsize()} of {queue.maxsize})')
                return
            except Full:
                logging.debug(f'no free chair in queue')
                pass

    def __str__(self):
        return self.name


for config in CONFIGS:
    logging.info("=" * 80)
    logging.info(f"New config {config}")

    clients = [Client(f"client #{i}/{config.CLIENTS}") for i in range(config.CLIENTS)]
    barbers = [Barber(f"Barber {i}") for i in range(config.BARBERS)]
    queue = Queue(maxsize=config.CHAIRS)
    is_closed = False

    for barber in barbers: barber.start()
    for client in clients: client.start()

    for client in clients: client.join()
    # we work til the last client
    is_closed = True

    status = ''.join(map(lambda x: '+' if x.served else '-', clients))
    logging.info(f"Finished serving config {config}. client status = {status}")

    # wait for barbers to finish their sleep
    for barber in barbers: barber.join()
