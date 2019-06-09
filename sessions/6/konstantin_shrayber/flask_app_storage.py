import json
from functools import wraps


def read_items(items: list):
    def decorator(source_function):
        @wraps(source_function)
        def read_wrapper():
            items.clear()
            with open('flask_app_storage.txt', 'r') as store:
                for line in store.readlines():
                    items.append(json.loads(line.strip()))
            return source_function()
        return read_wrapper
    return decorator


def write_items(items: list):
    def decorator(source_function):
        @wraps(source_function)
        def write_wrapper():
            result = source_function()
            with open('flask_app_storage.txt', 'w') as store:
                for item in items:
                    store.write(json.dumps(item) + '\n')
            return result
        return write_wrapper
    return decorator


def update_items(items: list):
    def decorator(source_function):
        @wraps(source_function)
        def write_wrapper(item_id):
            result = source_function(item_id)
            with open('flask_app_storage.txt', 'w') as store:
                for item in items:
                    store.write(json.dumps(item) + '\n')
            return result
        return write_wrapper
    return decorator
