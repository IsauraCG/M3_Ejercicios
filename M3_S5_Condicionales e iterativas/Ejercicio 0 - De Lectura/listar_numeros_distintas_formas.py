# Hay varias maneras.

# 1
from itertools import accumulate
from itertools import starmap
from itertools import tee
from functools import reduce
import itertools
# [print)(i) for i in range(10+1)]

# 2
i = 0
while i <= 100:
    print(i)
    i += 1

# 3
for i in (x for x in range(10+1)):
    print(i)

# 4
for i, _ in enumerate(range(10+1)):
    print(i)

# 5


def print_numbers(n):
    if n > 10:
        return
    print(n)
    print_numbers(n+1)


print_numbers(0)

# 6

for i in itertools.islice(itertools.count(), 10+1):
    print(i)

# 7
""" f = lambda x: x if x > 10 else (print(x), f(x+1)) 
f(0) """

# 8
list(map(print, range(10+1)))

# 9


def f(acc, x):
    print(x)
    return acc


reduce(f, range(10+1), None)


# 10
_, it = tee(range(10+1))
for i in it:
    print(i)

# 11
""" for i in starmap(lambda x: x, [(x,) for x in range(10+1)]):
    print(i) """

# 12
for i in accumulate(range(10+1), lambda acc, x: x):
    print(i)
