n = int(input())
seq = tuple(map(int, input().split()))


def solution(n, seq):
    norm = {}
    count = 0
    for i in range(n):
        sum = seq[i]
        j = i + 1
        while j < n and sum != 0:
            sum += seq[j]
            j += 1
        if sum == 0:
            count += n + 1 - j
            for l in range(i + 1):
                for r in range(j - 1, n):
                    norm.setdefault((l, r), True)
    return len(norm)


print(solution(n, seq))
