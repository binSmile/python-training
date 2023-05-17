with open('input.txt', 'r') as fin:
    x = int(fin.readline()) # число из первой строки
    seq = tuple(map(int,fin.readline().split(' '))) # все остальные строки




def solution(seq):
    bestprobe = -1
    best = max(seq)
    prevbest = -1
    for i in range(1, len(seq) - 1):
        prevbest = max(prevbest, seq[i-1])
        if ((seq[i] % 10) == 5) and \
                seq[i + 1] < seq[i] and \
                prevbest >= best:
            if seq[i] > bestprobe:
                bestprobe = seq[i]

    vrating = 1
    if bestprobe != -1:
        for i in seq:
            if i > bestprobe:
                vrating += 1
        return vrating

    else:
        return 0

print(solution(seq))


