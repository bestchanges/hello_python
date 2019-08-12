"""
It's UGLY and broken! Just keep it for a history.
"""
import logging
import random
from queue import Queue, Full, Empty
from threading import Thread, Condition
from time import sleep

NUM_CLIENTS = 5
NUM_CHAIRS = 5

logging.basicConfig(
    format='%(relativeCreated)6d [%(filename)s:%(lineno)3s] %(name)20s: %(message)s',
    # format='%(relativeCreated)6d %(name)20s (Thread: %(threadName)15s): %(message)s       [%(filename)s:%(lineno)s]',
    level=logging.INFO,
)

logging.info("TEST INFO")


class Barbershop:

    def __init__(self) -> None:
        self.seat = None
        self.is_open = False
        self.hairdresser = None
        self.logger = logging.getLogger('barbershop')
        self.queue = Queue(maxsize=NUM_CHAIRS)

    def open(self):
        self.logger.info("open")
        self.is_open = True
        self.hairdresser = Hairdresser(barbershop=self)
        self.hairdresser.start()

    def close(self):
        self.logger.info("closing")
        self.is_open = False
        awake_bell = self.hairdresser.awake_bell
        with awake_bell:
            self.logger.info("awaking hairdresser")
            awake_bell.notify()

    def client_takes_seat(self, client):
        assert self.seat is None
        client.state = 'sitting in front of hairdresser'
        self.seat = client

    def __str__(self) -> str:
        return f"hairdresser={self.hairdresser}, seat={self.seat}, queue={self.queue}"


class Client(Thread):

    def __init__(self, name) -> None:
        super().__init__(name=name)
        self.logger = logging.getLogger(f"Client: {name}")
        self.hair = "mess"
        self._state = "Pending"

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self.logger.info(f'set state to {value}')
        self._state = value

    def walk_out(self):
        self.state = 'walking out'
        time = random.random() * 4
        self.logger.info(f'{self.state} for {time:.2f}')
        sleep(time)

    def take_a_haircut(self):
        self.state = 'came to barbershop'
        if barbershop.hairdresser.state == 'sleeping':
            self.logger.info(f'found sleeping hairdresser')
            awake_bell = barbershop.hairdresser.awake_bell
            with awake_bell:
                barbershop.client_takes_seat(self)
                self.logger.info(f'ringing the bell')
                awake_bell.notify()
                return True
        else:
            self.state = 'try taking the queue'
            self.logger.info(f'Queue size: {barbershop.queue.qsize()}')
            try:
                barbershop.queue.put(self, block=False)
                self.state = 'waiting in queue'
            except Full:
                return False

    def run(self):
        while True:
            self.walk_out()
            if self.hair != 'mess':
                return
            if barbershop.is_open:
                self.take_a_haircut()
            else:
                self.state = 'unhappy'
                return

    def __str__(self) -> str:
        return f"{self.name}"


class Hairdresser(Thread):

    def __init__(self, barbershop) -> None:
        super().__init__(name="Hairdresser")
        self._state = "Pending"
        self.logger = logging.getLogger("Hairdresser")
        self.barbershop = barbershop
        self.awake_bell = Condition()

    def run(self):
        self.logger.info("Start working")
        self.state = 'ready to work'
        while True:
            if not barbershop.is_open:
                self.logger.info("The barbershop is closed so I go home")
                return
            while self.service_client_from_queue():
                pass
            self.sleep_until_awake()

    def service_client_in_seat(self):
        assert self.barbershop.seat is not None
        assert self.state == 'ready to work'
        client = self.barbershop.seat
        self.logger.info(f"going to service {client}")
        client.state = 'having a haircut'
        self.state = 'working'
        sleep(1)
        self.state = 'finish job'
        client.state = 'happy'
        client.hair = 'nice'
        self.logger.info(f"Finish servicing {client}")
        # TODO: What about locks
        self.state = 'ready to work'
        self.barbershop.seat = None

    def service_client_from_queue(self):
        try:
            barbershop.seat = barbershop.queue.get(block=False)
            self.service_client_in_seat()
            barbershop.queue.task_done()
            return True
        except Empty:
            self.logger.info("No clients in queue")
            return False

    def sleep_until_awake(self):
        self.state = 'sleeping'
        with self.awake_bell:
            self.awake_bell.wait()
            self.state = 'awoken'
            self.state = 'ready to work'
            if barbershop.seat is not None:
                self.service_client_in_seat()

    def __str__(self) -> str:
        return f"Hairdresser is {self.state}"

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self.logger.info(f'set state to {value}')
        self._state = value


barbershop = Barbershop()
clients = [Client(f"client #{i}") for i in range(NUM_CLIENTS)]

barbershop.open()

for client_thread in clients:
    client_thread.start()

sleep(5)
barbershop.close()
barbershop.hairdresser.join()
for client in clients:
    client.join()
