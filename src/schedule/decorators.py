from time import sleep


def schedule(timeout = 5):
    def wrapper(func):
        def inner(*args, **kwargs):
            while True:
                func(*args, **kwargs)
                sleep(timeout)
        return inner
    return wrapper


def logger(func):
    def inner(*args, **kwargs):
        print('Start refreshing')
        func(*args, **kwargs)
        print('End refreshing')
    return inner