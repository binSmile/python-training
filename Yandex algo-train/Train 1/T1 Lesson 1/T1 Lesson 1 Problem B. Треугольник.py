# a = int(input())
# b = int(input())
# c = int(input())


def solution(a, b, c):
    sidelist = [a, b, c]
    if 0 in sidelist:
        return 'NO'

    sidelist.sort()

    if sidelist[0] + sidelist[1] > sidelist[2]:
        return 'YES'
    else:
        return 'NO'


# print(solution(a, b, c))
print(solution(3,4,5) == 'YES')