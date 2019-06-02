import builtins

x = 'global x'

def f():
    # global x
    # x = "local x"
    z = 18
    print(z)
    x = x + 'y'
    print(x)


# print(x)

million = 1_000_000

print(type(million))
print(million)


class cm:
    def __enter__(self):
        self._max = builtins.max
        builtins.max = None
        print('enter')

    def __exit__(self, *args):
        builtins.max = self._max
        print('exit')

with cm() as some:
    #max([1,2])
    pass
max([1,2])