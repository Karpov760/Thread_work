from time import sleep
from threading import Condition, Thread
from concurrent.futures import ThreadPoolExecutor
import multiprocessing
from multiprocessing import Pool
from queue import Queue

class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

x = 1
sum = 0
N = 5


def fuct(n):
    if n == 0:
        n = 1
    if n > 0:
        for i in range(1, n):
            n *= i
    return n

def deg(n):
    return x ** n

def Makloren_line(n): # numbers of iterations
    global sum
    for i in range(0, n):
        twrv = ThreadWithReturnValue(target=deg, args=(i,))
        twrf = ThreadWithReturnValue(target=fuct, args=(i,))
        twrv.start()
        twrf.start()
        d = twrv.join()
        f = twrf.join()
        sum += d / f
        print(sum)

    return sum

def foo(bar):
    return "foo"

print(Makloren_line(6))










