# Task: find a values of recurrent sequence

import random

#initial variables
n = 10 # random.randint(1,1000)
numbers = [0,1,2,3,4,5]



from functools import lru_cache
@lru_cache()
def f(k):
    match k:
        case 0:
            return 0
        case 1:
            return 2
        case 2:
            return 2
        case _:
            return  f(k-1) + f(k-3)
def soluion_slow(numbers):
    for i in numbers:
        print(f(i), end=' ')


soluion_slow(numbers)


def habr_solution():
    # n = int(input())
    indices = [int(i) for i in input().split()]
    results = {i: i if i < 3 else None for i in indices}
    k = max(indices)
    a, b, c = 0, 1, 2
    for i in range(3, k + 1):
        a, b, c = b, c, a + c
        if i in results:
            results[i] = c
    print(" ".join(str(results[i]) for i in indices))

habr_solution()