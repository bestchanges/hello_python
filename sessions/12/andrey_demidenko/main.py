
class ZipWithDefaults:
    def __init__(self, default=None):
        self.default_zip_value = default
        self.zip = __builtins__.zip

    def __enter__(self):
        __builtins__.zip = self.zip_with_default

    def __exit__(self, exc_type, exc_val, exc_tb):
        __builtins__.zip = self.zip

    def zip_with_default(self, *args):
        length = max([len(el) for el in args])
        for index in range(length):
            yield tuple(el[index] if len(el) > index else self.default_zip_value for el in args)


if __name__ == '__main__':
    a = 'Python'
    b = [10, 11, 12]
    print('Builtin Zip function result: ')
    print(list(zip(a, b)))
    with ZipWithDefaults():
        print('Zip function with default None value result: ')
        print(list(zip(a, b)))
    with ZipWithDefaults('empty'):
        print('Zip function with default \'empty\' value result: ')
        print(list(zip(a, b)))
    print('Builtin Zip function result again: ')
    print(list(zip(a, b)))
