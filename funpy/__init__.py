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