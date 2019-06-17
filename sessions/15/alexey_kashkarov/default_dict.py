class MyDefaultDict(dict):
    def __init__(self, default_type=int):
        self.default_factory = default_type

    def __missing__(self, key):
        return self.default_factory()


dd = MyDefaultDict(list)
print(dd['key'])
