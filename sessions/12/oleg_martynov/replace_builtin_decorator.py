from contextlib import contextmanager


@contextmanager
def replace_builtin(src_name, new_func):
    old_func = globals()["__builtins__"].__getattribute__(src_name)
    globals()["__builtins__"].__setattr__(src_name, new_func)
    yield
    globals()["__builtins__"].__setattr__(src_name, old_func)


print(pow(2, 6))

with replace_builtin("pow", lambda *x: 666):
    print(pow(2, 6))

print(pow(2, 6))
