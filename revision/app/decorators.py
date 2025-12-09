import time


def timer(func):
    def wrapper(*args, **kwargs):
        time_before = time.time()
        result = func(*args, *kwargs)
        final_time = time.time() - time_before
        print(f'{func.__name__} took {final_time} seconds')
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(5)

@timer
def fast_function():
    time.sleep(0.5)

timer(slow_function())
timer(fast_function())




