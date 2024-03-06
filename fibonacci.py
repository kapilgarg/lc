# fibonacci using reduce

from functools import reduce
def fib(n):
    if n < 2:
        return n
    return reduce(lambda v, e: (v[1], v[1] + v[0]), range(1, n), (0, 1))[1]
