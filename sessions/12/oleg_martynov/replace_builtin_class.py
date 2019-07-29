class ReplaceBuiltin():
    def __init__(self, src_function_name, replacing_func):
        self.__src_function_name = src_function_name
        self.__replacing_func = replacing_func

    def __enter__(self):
        self.__backup = globals()["__builtins__"].__getattribute__(self.__src_function_name)
        globals()["__builtins__"].__setattr__(self.__src_function_name, self.__replacing_func)

    def __exit__(self, exc_type, exc_val, exc_tb):
        globals()["__builtins__"].__setattr__(self.__src_function_name, self.__backup)


with ReplaceBuiltin("pow", lambda x, y: x * y):
    print(pow(2, 5))

print(pow(2, 5))

