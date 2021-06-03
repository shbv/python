import time
import numpy as np

class Timer():

    def __init__(self):
        self.tick = time.time()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        tock = time.time()
        runtime = tock - self.tick
        print(f"time: {runtime} secs")


def func():
    x = np.random.rand(20,30)
    y = np.random.rand(30,20)
    print(np.matmul(x,y).shape)


if __name__ == '__main__':
    with Timer():
        func()
