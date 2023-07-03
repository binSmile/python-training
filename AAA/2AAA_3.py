import math
from scipy.integrate import quad

################################################
#
# 2nd stage
# Task 3: see 2AAA_3_description.md
#
################################################


def solution(n):
    # Function f(x)
    def f(x):
        return math.sin(x) / (math.sin(x) + 2)

    # Calculation of coefficients
    a = []
    b = []

    a0, error = quad(f, -math.pi, math.pi)
    a.append(round((a0 / math.pi),3))

    for i in range(1, n + 1):  # iteration from 1 to n
        # a_n
        result, error = quad(lambda x: f(x) * math.cos(i * x), -math.pi, math.pi)
        a.append(round((result / math.pi),3))

        # b_n
        result, error = quad(lambda x: f(x) * math.sin(i * x), -math.pi, math.pi)
        b.append(round((result / math.pi), 3))

    return [a,b]


assert solution(2) == [[-0.309, -0.0, 0.166],[0.619, 0.0]]


def main():
    n = int(input())

    for k in solution(n):
        print(' '.join(map(str,k)))

if __name__ == '__main__':
    main()



