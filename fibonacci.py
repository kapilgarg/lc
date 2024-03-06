# fibonacci using reduce

from functools import reduce
def fib(n):
    if n < 2:
        return n
    return reduce(lambda v, e: (v[1], v[1] + v[0]), range(1, n), (0, 1))[1]

print(timeit('fib(100)', setup="from __main__ import fib "))
>>>23.8715282


# fibonacci using loop
def fib2(n):
    a, b = 0, 1
    if n < 2:
        return n
    for _ in range(2, n + 1):
        nextnum = a + b
        a, b = b, nextnum
    return nextnum

print(timeit('fib2(100)', setup="from __main__ import fib2 "))
>>>8.202182800000003

# fibonacci using recursion
def fib3(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(timeit('fib3(100)', setup="from __main__ import fib3 "))
>>>46.726457800000006
