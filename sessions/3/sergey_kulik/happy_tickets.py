import random


def generate_num_array():
    a = []
    for x in range(0, 6):
        a.append(random.randint(0, 9))
    return a


def num_array_to_str(numArray):
    return ''.join(str(s) for s in numArray)


def is_lucky():
    while True:
        numArray = generate_num_array()
        if sum(numArray[0:3]) == sum(numArray[3:6]):
            yield num_array_to_str(numArray)


print(next(is_lucky()))
