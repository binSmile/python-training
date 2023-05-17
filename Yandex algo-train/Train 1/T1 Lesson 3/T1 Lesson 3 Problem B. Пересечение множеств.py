
seq1 = map(int, input().split())
seq2 = map(int, input().split())

def intersection(list_a, list_b):
    return sorted(set(list_a) & set(list_b))



print(*intersection(seq1, seq2))