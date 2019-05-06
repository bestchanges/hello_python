#!/usr/bin/env python3

# TDD demo
# run this via:
#      $ pytest tdd.py


def add(x, y):
    return x + y


def test_add1_2():
    assert add(1, 2) == 3


def test_add33():
    assert add(1, 2) == 33   # Fail here
