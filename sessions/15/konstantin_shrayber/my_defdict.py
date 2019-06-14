from collections import defaultdict


class MyKeyDefDict(defaultdict):
    def __init__(self, func):
        super().__init__(None)
        self.func = func

    def __missing__(self, key):
        res = self.func(key)
        self[key] = res
        return res


def factorial(x):
    if x == 0:
        return 1
    else:
        x * factorial(x - 1)


mdd = MyKeyDefDict(lambda x: factorial(x))

for i in range(7):
    mdd[i]

print(mdd)