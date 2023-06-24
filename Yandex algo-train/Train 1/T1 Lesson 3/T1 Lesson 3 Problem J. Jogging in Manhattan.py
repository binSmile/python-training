# Link to task
# https://contest.yandex.ru/contest/27663/problems/J/
# Algorithm
#
# Asymptotic


def make_exp_map(x0,y0,d):
    prev_pointsx, prev_pointsy = [], []
    for i in range(-d, d + 1):
        for j in range(d):
            if abs(i) + abs(i) <= d:
                prev_pointsx.append(x0 + i)
                prev_pointsy.append(y0 + j)
    return (prev_pointsx, prev_pointsy)
def solution(t,d,n,points):
    if d < t*1:
        expectation = []
        maybemap_pp = make_exp_map(*points[-2],d)
        maybemap_p = make_exp_map(*points[-1], d)
        for i in range(len(maybemap_pp[0])):
            for j in range(len(maybemap_p[0])):
                if abs(i[0]-j[0])+abs(i[1]-j[1]) <= t:
                    expectation.append(maybemap_p[j])


assert solution(2, 1, 5, [(0, 1), (-2, 1), (-2, 3), (0, 3), (2, 5)] ) == (2,(1,5),(2,4))
assert solution(1, 1, 1, [(0, 0)] ) == (5,(-1, 0),(0, -1),(0, 0),(0, 1),(1, 0))
assert solution(1, 10, 1, [(0, 0)] ) == (5,(-1, 0),(0, -1),(0, 0),(0, 1),(1, 0))

def main():
    t,d,n = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    solution(t,d,n,points)

if __name__ == '__main__':
    main()


