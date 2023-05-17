seq = tuple(map(int,input().split(' ')))

def solution(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])

    min2 = max(seq[0], seq[1])
    min1 = min(seq[0], seq[1])

    for i in range(2,len(seq)):
        v = seq[i]
        if v >= max1 and v > max2:
            max2 = max1
            max1 = v
        elif max1 > v > max2:
            max2 = v

        if v <= min1 and v < min2:
            min2 = min1
            min1 = v
        elif min1 < v < min2:
            min2 = v

    if max1 * max2 > min1 * min2:
        return (max2, max1)
    else:
        return (min1, min2)

print(*solution(seq))