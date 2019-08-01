import logging
import random
import time
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
    Config(CLIENTS=20, CHAIRS=10, BARBERS=3),
    Config(CLIENTS=20, CHAIRS=5, BARBERS=3),
    Config(CLIENTS=20, CHAIRS=2, BARBERS=3),
)

logging.basicConfig(
    format='%(relativeCreated)6d %(threadName)15s: %(message)s',
    level=logging.WARNING,
)


class Barber(Thread):
    def __init__(self, name) -> None:
        super().__init__(name=name)

    def run(self):
        while True:
            try:
                client = queue.get(timeout=0.3) # type: Client
                logging.info(f'serving {client}')
                sleep(0.5)
                client.served = True
                logging.debug(f'finish serving {client}')
                # I use notification for client when job is done just for example
                with client.awaited:
                    client.awaited.notify()
            except Empty:
                logging.debug(f"I've been sleeping for a while. And there are no any clients come")
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
            walk_time = (random.random() + 0.2) * 0.3
            logging.debug(f'I heading to barbershop. I takes {walk_time:.2f} seconds to come')
            sleep(walk_time)
            # You can test with failing Client threads
            # if random.randint(1,6) == 2:
            #     raise ArithmeticError()
            try:
                queue.put(self, timeout=0.1)
                logging.info(f'start waiting in the queue (queue length={queue.qsize()} of {queue.maxsize})')
                with self.awaited:
                    self.awaited.wait()
                logging.debug(f'I has my hair cut! (queue length={queue.qsize()} of {queue.maxsize})')
                return
            except Full:
                walk_time = (random.random() + 1.2) * 1.3
                logging.debug(f'no free chair in queue, so I go to walk for {walk_time:.2f} seconds')
                sleep(walk_time)

    def __str__(self):
        return self.name


for config in CONFIGS:
    logging.warning("=" * 80)
    logging.warning(f"New config {config}")

    clients = [Client(f"client #{i}/{config.CLIENTS}") for i in range(config.CLIENTS)]
    barbers = [Barber(f"Barber {i}") for i in range(config.BARBERS)]
    queue = Queue(maxsize=config.CHAIRS)
    is_closed = False

    for barber in barbers: barber.start()
    start_time = time.time()
    for client in clients: client.start()

    for client in clients: client.join()
    end_time = time.time()
    # we work til the last client
    is_closed = True

    status = ''.join(map(lambda x: '+' if x.served else '-', clients))
    logging.info(f"Finished serving config {config}. client status = {status}")

    # wait for barbers to finish their sleep
    for barber in barbers: barber.join()
    duration = end_time - start_time
    logging.warning(f"It took {duration:.2} seconds (average {duration / config.CLIENTS * config.BARBERS:.2f} sec per client)")
