# ---------------------------
# Limiter
# ---------------------------

from typing import List


class LimitedFunc:
    startCount: int
    count: int

    def __init__(self, count, func) -> None:
        super().__init__()
        self.count, self.startCount = count, count
        self.func = func

    def __call__(self, *a, **k):
        if self.count > 0:
            res = self.func(*a, *k)
            self.count -= 1
            return res

    def reset(self):
        self.count = self.startCount


# Calls a function only n-times until reset()
def limited(n):
    def dec(f):
        lf = LimitedFunc(n, f)
        return lf
    return dec

# ---------------------------
# Repeater
# ---------------------------


def repeat(n):
    def deco(f):
        def wrapper(*a, **k):
            arr = []
            for i in range(n):
                arr.append(f(*a, **k))
            return arr
        return wrapper
    return deco

# ---------------------------
# ReturnExpand
# ---------------------------


def tupleTwice(f):
    def wrapper(*a, **k):
        res = f(*a, **k)
        return (res, res)
    return wrapper

# ---------------------------
# ForEachArg
# ---------------------------


def forEachArg(func):
    def wrapper(*a):
        arr = []
        for i in range(len(a)):
            arr.append(func(a[i], i))
        return arr
    return wrapper

# ---------------------------
# Executor
# ---------------------------


def executeWith(executor):
    def deco(func):
        def wrapper(*a, **k):
            def call():
                return func(*a, **k)
            return executor(call)
        return wrapper
    return deco

# ---------------------------
# Nullable
# ---------------------------


class Maybe:
    def __init__(self, data) -> None:
        self.data = data

    def orElse(self, els):
        if self.data == None:
            return els
        return self.data

    def get_val(self):
        if self.data == None:
            raise ValueError("Data is absent")
        return self.data

    def process(self, func):
        if self.data != None:
            func(self)
        return self

    def map(self, mapper):
        if self.data != None:
            newDat = mapper(self.data)
            return Maybe(newDat)
        return Maybe(None)

    def orGet(self, getter):
        if self.data != None:
            return self.data
        return Maybe(getter(self))

# ---------------------------
# Elements
# ---------------------------
from random import randint as __rand

def get_random(elems):
    if elems == None or len(elems) < 1:
        return None
    return elems[__rand(0, len(elems)-1)]

# ---------------------------
# Multiple Func call
# ---------------------------
def one_of(args, *funcs):
    for f in funcs:
        res = f(*args)
        if res != None:
            return res