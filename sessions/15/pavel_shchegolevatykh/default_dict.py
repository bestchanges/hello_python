class MyDefaultDict(dict):

    def __init__(self, *args, **kwargs):
        self.default = kwargs.pop('default', None)
        dict.__init__(self, *args, **kwargs)

    def __missing__(self, key):
        if self.default:
            return self.default(key)
        else:
            raise KeyError(key)

    def __getitem__(self, key):
        try:
            return dict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)


iceCreamLovers = MyDefaultDict(default=lambda key: 'Vanilla')

iceCreamLovers['Bill'] = 'Chocolate'
iceCreamLovers['Will'] = 'Banana'

print(iceCreamLovers['Bill'], iceCreamLovers['Will'], iceCreamLovers['Amy'])

