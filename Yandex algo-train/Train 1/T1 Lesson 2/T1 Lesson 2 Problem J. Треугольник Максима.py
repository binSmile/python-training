n = int(input())
seq = []
S = float(input())
for i in range(1,n):
    inl = input().split(' ')
    seq.append((float(inl[0]),inl[1]))

R = 4000
L = 30

def solution(S,seq, L, R):
    for i in range(len(seq)):
        t = seq[i]
        if i >= 1:
            S = seq[i-1][0]
        if abs(S - t[0]) < 10**(-6):
            continue

        if t[1] == 'closer':
            if t[0] < S:
                # side = 'left'
                L = L
                R = min(R, S - abs(S - t[0]) / 2)
            else:
                # side = 'right'
                R = R
                L = max(L, S + abs(S - t[0]) / 2)

        else:
            if t[0] < S:
                # side = 'left'
                R = R
                L = max(L, t[0] + abs(S-t[0])/2)
            else:
                # side = 'right'
                L = L
                R = min(R, S + abs(t[0]-S)/2)
        S = t[0]
    return L,R

print(*solution(S, seq, L, R))

