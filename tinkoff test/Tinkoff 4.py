n = int(input())
s = tuple(map(int,input().split()))


def solution(n,s):
    td = {}
    l = 0
    for i in range(n):
        td[s[i]] = td.setdefault(s[i], 0) + 1
        sv = tuple(td.values())
        ssv = tuple(set(sv))
        if len(ssv) == 1:
            l = max(i + 1, l)
        elif (len(ssv) == 2):
            ttd = {}
            for j in sv:
                ttd[j] = ttd.setdefault(j, 0) + 1
            ttd_val = ttd.values()
            if (min(ttd_val) == 1):
                l = max(i + 1, l)
    return l

print(solution(n,s))