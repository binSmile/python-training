# Link to task
# https://contest.yandex.ru/contest/27663/problems/F/
# Algorithm
# 1. make dict with count from pairs for first genome
# 2. make set of pairs for second genome
# 3. get a sum of counts from 1st dict by keys from second set
# Asymptotic

def solution(g1, g2):
    #best, reference https://github.com/Yankovsky/yandex-algos-training/blob/master/hw3/f.py
    # 1. make set of pairs from 2nd genome
    # 2. check 1st genomes pairs and sum
    g2_pairs = set()
    compare = 0

    if len(g1) > 1 and len(g2) > 1:
        for i in range(len(g2)-1):
            g2_pairs.add(g2[i:i+2])

        for i in range(len(g1)-1):
            if g1[i:i+2] in g2_pairs:
                compare += 1

    return compare


def solution_slow(g1, g2):
    g1_pairs = {}
    g2_pairs = set()
    compare = 0

    if len(g1) > 1 and len(g2) > 1:
        for i in range(len(g1)-1):
            d = g1[i:i+2]
            g1_pairs[g1[i:i+2]] = g1_pairs.setdefault(g1[i:i+2],0) + 1
        for i in range(len(g2)-1):
            g2_pairs.add(g2[i:i+2])

        for i in g2_pairs:
            compare += g1_pairs.setdefault(i,0)
    return compare



assert solution('ABBACAB', 'BCABB') == 4
# test for solution('ABC','A')


def main():
    g1 = input()
    g2 = input()
    print(solution(g1, g2))


if __name__ == '__main__':
    main()



