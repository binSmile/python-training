with open('input.txt', 'r') as fin:
    # N = int(fin.readline()) # число из первой строки
    seq = tuple(map(int,fin.readlines()[0].rstrip().split(' ')))


def MySort(seq):
    if len(seq) <= 1:
        return seq
    else:
        b_seq, e_seq, a_seq = [],[],[]
        e = (max(seq)+min(seq))/2
        for i in seq:
            if i < e:
                b_seq.append(i)
            elif i > e:
                a_seq.append(i)
            else:
                e_seq.append(i)
        return MySort(b_seq) + e_seq + MySort(a_seq)

def solution(seq):
    seq = MySort(seq)
    v1 = seq[-2] * seq[-3] * seq[-1]
    v2 = seq[0] * seq[1] * seq[-1]
    if v1 > v2:
        return (seq[-1],seq[-2],seq[-3])
    else:
        return (seq[-1], seq[0], seq[1])

print(*solution(seq))

