with open('input.txt', 'r') as fin:
    # N = int(fin.readline()) # число из первой строки
    seq = tuple(map(int,fin.readlines()[0].rstrip().split(' ')))


def solutin(seq):
    s = set(seq)
    return len(s)

print(solutin(seq))