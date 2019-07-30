class DefaultDict(dict):

    def __init__(self, fn_def):
        super().__init__()
        self.__fn_def = fn_def

    def get(self, k):


        value = super().get(k)

        if not value:
            value = self.__fn_def()

        return value


default_dict = DefaultDict(lambda: "empty")

default_dict.update({"a": 1, "b": 2, "c": 3})

print(default_dict)

print(f"existing key a: {default_dict.get('a')}, non-existing key d: {default_dict.get('d')}")
