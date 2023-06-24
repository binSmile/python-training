# Link to task
# https://contest.yandex.ru/contest/27663/problems/G/
# Algorithm
#

def solution(N, ABlist):
    truthful = 0
    ABlist = list(set(ABlist))
    for i in range(len(ABlist)):
        a,b = ABlist[i]
        if a + b + 1 == N and a >= 0 and b >= 0:
            truthful += 1
    return truthful



assert solution(3, [(2, 0), (0, 2), (2, 2)]) == 2
assert solution(5, [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]) == 5
assert solution(10, [(9, 1), (8, 1), (7, 2), (6, 2), (5, 3), (4, 4), (3, 6), (2, 7), (1, 9), (0, 8)]) == 4

assert solution(1, [(0,0)]) == 1
assert solution(1, [(0,0)]) == 1
assert solution(2, [(0,0),(0,0)]) == 0

def read_test_data(n):
    with open('T1 Lesson 3 Problem G. Turtles. Test data {}'.format(n), 'r') as f:
        read_data = f.readlines()
        N = int(read_data[0])
        ABlist = []
        for line in read_data[1:]:
            ab = tuple(map(int, line.split()))
            ABlist.append(ab)
    return (N, ABlist)

assert solution(*read_test_data(4)) == 2811
assert solution(*read_test_data(10)) == 1540

def main():
    N = int(input())
    ABlist = []
    for _ in range(N):
        ab = tuple(map(int,input().split()))
        ABlist.append(ab)
    print(solution(N, ABlist))

if __name__ == '__main__':
    main()
