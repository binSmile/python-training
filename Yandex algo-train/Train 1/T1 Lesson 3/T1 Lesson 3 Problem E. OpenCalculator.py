# Link to task
# https://contest.yandex.ru/contest/27663/problems/E/

def solution(xyz, N):
    xyz = set(xyz.split())
    N = set(N)

    return len(set.union(xyz,N)) - len(xyz)



assert solution('1 2 3', '1123') == 0
assert solution('1 2 3', '1001') == 1
assert solution('5 7 3', '123') == 2



def main():
    xyz = input()
    N = input()
    print(solution(xyz, N))


if __name__ == '__main__':
    main()



