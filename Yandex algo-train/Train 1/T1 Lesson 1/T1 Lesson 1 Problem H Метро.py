a = int(input())
b = int(input())
n = int(input())
m = int(input())

# a = 1 # интервал на первом пути между поездами
# b = 3 # интервал на втором пути между поездами
# n = 3 # количество увиденных на первом пути
# m = 2 # количество увиденных на втором пути

def solution(a,b,n,m):
    mina = n*1 + (n-1)*a
    minb = m*1 + (m-1)*b

    maxa = mina + 2 * a
    maxb = minb + 2 * b
    if maxa < minb or maxb < mina:
        return -1
    else:
        return '%s %s' % (max(mina,minb), min(maxa,maxb))

print(solution(a,b,n,m))
# print(solution(1,3,3,2) == '5 7')
# print(solution(1,5,1,2) == -1)
# print(solution(1,5,1,2))