import random
import time
import functools
import numpy as np

def timer(func):
    "timer docstring"
    @functools.wraps(func)
    def func_timer(*args, **kwargs):
        "func_timee docstring"
        tick = time.time()
        value = func(*args, **kwargs)
        tock = time.time()
        runtime = tock - tick
        print(f"{func.__name__} took {runtime} secs")
        return value
    return func_timer


@timer
def func():
    x = np.random.rand(20,30)
    y = np.random.rand(30,20)
    print(np.matmul(x,y).shape)

if __name__ == '__main__':
    func()
