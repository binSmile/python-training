a, b, c, d = tuple(map(int, input().split()))


def solution(a, b, c, d):
    if a >= b >= c >= d or \
            a <= b <= c <= d:
        return 'YES'
    else:
        return 'NO'

print(solution(a, b, c, d))