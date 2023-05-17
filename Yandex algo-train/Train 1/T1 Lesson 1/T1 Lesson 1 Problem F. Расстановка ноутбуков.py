params = map(int,input().split(' '))

def slowsol(a1,a2,b1,b2):

    l1 = a1 + b1  # 7 + 3
    l2 = max(a2, b2)  # 5 (2)
    s = l1 * l2

    ll1 = a1 + b2  # 7 + 2 ## BEST
    ll2 = max(a2, b1)  # 5 (3)
    ss = ll1*ll2
    if ss < s:
        l1 = ll1
        l2 = ll2
        s = ll1 * ll2

    ll1 = a2 + b1  # 5 + 3
    ll2 = max(a1, b2)  # 7 (2)
    ss = ll1*ll2
    if ss < s:
        l1 = ll1
        l2 = ll2
        s = ll1 * ll2

    ll1 = a2 + b2  # 5 + 2
    ll2 = max(a1, b1)  # 7 (3)
    ss = ll1*ll2
    if ss < s:
        l1 = ll1
        l2 = ll2
        s = ll1 * ll2

    return l1, l2

def solution(a1,a2,b1,b2):
    if a1 < a2:
        a1, a2 = a2, a1
    if b1 < b2:
        b1, b2 = b2, b1

    # l1 = max(a1,b1)
    # l2 = a2 + b2

    l1 = max(a2,b1) # 5
    l2 = a1 + b2 # 9
    return l1, l2

print(*slowsol(*params))


