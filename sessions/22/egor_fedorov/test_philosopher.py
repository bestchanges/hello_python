import pytest

from philosophers import Philosopher, Fork, StateError, create_philosophers


def test_philosopfer():
    philosopher = Philosopher("Diogen")
    fork1 = Fork(1)
    fork2 = Fork(2)
    philosopher = Philosopher("Diogen", fork2, fork1)
    assert philosopher is not None
    assert str(philosopher) == "Diogen"
    assert philosopher.is_hungry

    philosopher = Philosopher("Diogen", fork2, fork1)
    assert philosopher.forks == [fork1, fork2]
    philosopher = Philosopher("Diogen", fork1, fork2)
    assert philosopher.forks == [fork1, fork2]


def test_fork():
    fork = Fork(1)
    assert fork
    assert str(fork) == "Fork(1)"
    philosopher1 = Philosopher("Diogen", fork, fork)
    philosopher2 = Philosopher("Platon", fork, fork)
    assert fork.take_by(philosopher1)
    with pytest.raises(StateError):
        fork.take_by(philosopher2)


def test_eat():
    fork1 = Fork(1)
    fork2 = Fork(2)
    philosopher = Philosopher("Diogen", fork1, fork2)
    philosopher2 = Philosopher("Platon", fork2, fork1)
    philosopher.eat()
    assert not fork1.taken
    assert not fork2.taken
    fork1.take_by(philosopher2)
    with pytest.raises(StateError):
        philosopher.eat()


def test_deadlock():
    fork1 = Fork(1)
    fork2 = Fork(2)
    diogen = Philosopher("Diogen", fork1, fork2)
    platon = Philosopher("Platon", fork2, fork1)
    fork1.take_by(diogen)
    fork2.take_by(platon)
    with pytest.raises(StateError):
        fork2.take_by(diogen)
    with pytest.raises(StateError):
        fork1.take_by(platon)


def test_create_philosophers():
    philosophers = create_philosophers(("a", "b", "c"))
    assert len(philosophers) == 3

    p1 = philosophers[0]
    assert p1.name == "a"
    assert len(p1.forks) == 2
    assert p1.forks[0].number == 1
    assert p1.forks[1].number == 3

    p2 = philosophers[1]
    assert p2.name == "b"
    assert len(p2.forks) == 2
    assert p2.forks[0].number == 1
    assert p2.forks[1].number == 2

    p3 = philosophers[2]
    assert p3.name == "c"
    assert len(p3.forks) == 2
    assert p3.forks[0].number == 2
    assert p3.forks[1].number == 3
