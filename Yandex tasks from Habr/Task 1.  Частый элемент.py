# Task: Find the number that appears most frequently in the array.

import random
# len of array
n = 10
# Init array
numbers = [random.randint(1,10) for _ in range(n)]
print(numbers)
def solution(numbers):
    ram =  dict.fromkeys(set(numbers),0)
    ans = False
    ans_c = 0
    for n in numbers:
        ram[n] += 1
        if ans_c < ram[n]:
            ans_c = ram[n]
            ans = n
    return ans

print(solution(numbers))
