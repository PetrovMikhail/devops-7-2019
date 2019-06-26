import time
from functools import wraps


def delay(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        time.sleep(7)
        return function(*args, **kwargs)

    return wrapper
