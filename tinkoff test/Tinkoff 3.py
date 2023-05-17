n = int(input())
s = input()

def solution(s,n):
    best = 3e5
    for i in range(n):
        counter = 0
        t = {'a':False, 'b':False, 'c':False, 'd':False}
        while (counter+i < n)  and not (t['a'] and t['b'] and t['c'] and t['d']):
            t[s[counter+i]] = True
            counter += 1
        if (t['a'] and t['b'] and t['c'] and t['d']):
            best = min(best, counter)

    if best == 3e5:
        return -1
    else:
        return best

print(solution(s,n))


