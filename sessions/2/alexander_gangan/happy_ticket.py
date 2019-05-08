import random


def generate_lucky_ticket():
    """Returns a list of 6 ints where sum of first 3 digits equals to the last 3 digits"""
    lucky = False
    while not lucky:
        ticket = [random.randint(0,9) for i in range(6)]
        lucky = False if sum(ticket[:3]) - sum(ticket[3:]) else True
    return ticket


print(*generate_lucky_ticket())
