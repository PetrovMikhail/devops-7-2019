import time


def delay(function):
    def wrapper(*args, **kwargs):
        time.sleep(7)
        function()

    return wrapper
