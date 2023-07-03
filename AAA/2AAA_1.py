################################################
#
# 2nd stage
# Task 1: left Riemann sum
# Calculation of integral by left Riemann sum method.
# function: a*x**3 + b*x**2 + c*x + d
#
# input:
# 1st line: a,b,c,d
# 2nd line: start and end of integration interval
# 3rd line: count of intervals
#
################################################

def f(x,a,b,c,d):
    return a*x**3 + b*x**2 + c*x + d

def solution(a,b,c,d,K,M,N):
    sum = 0
    dx = abs((M-K)/N)
    for i in range(N):
        L = K + i*dx
        R = K + (i+1)*dx
        sum += f(L,a,b,c,d)
    sum *= dx
    return round(sum,3)


assert solution(1,2,3,4,0,2,1000) == 23.311


def main():
    a,b,c,d = map(float,input().split())
    K,M = map(float,input().split())
    N = int(input())

    print(solution(a,b,c,d,K,M,N))


if __name__ == '__main__':
    main()


