# Link to task
# https://contest.yandex.ru/contest/27663/problems/H/
# Algorithm
#
# Asymptotic

def solution(xlist, ylist):
    pulses = set(xlist)
    return len(pulses)


def test_show(xlist,ylist):
    import matplotlib.pyplot as plt
    plt.scatter(xlist,ylist)
    plt.show()

assert solution([1, 2, 3, 2, 3, 3] ,  [1, 2, 3, 1, 2, 1] ) == 3
assert solution([1, 2, 3, 2, 3, 3] ,  [1, 2, 3, 1, 2, 4] ) == 3




def main():
    N = int(input())
    xlist, ylist = [],[]
    for _ in range(N):
        x,y = map(int,input().split())
        xlist.append(x)
        ylist.append(y)
    print(solution(xlist,ylist))
    # test_show(xlist,ylist)

if __name__ == '__main__':
    main()

