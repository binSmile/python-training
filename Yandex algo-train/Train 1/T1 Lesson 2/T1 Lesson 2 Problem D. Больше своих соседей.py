seq = list(map(int, input().split(' ')))

def solution(seq):
    counter = 0
    if len(seq) > 2:
        for i in range(1,len(seq)-1):
            if seq[i - 1] < seq[i] > seq[i + 1]:
                counter+=1
    return counter

print(solution(seq))