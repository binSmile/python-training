# Link to task
# https://contest.yandex.ru/contest/27663/problems/I/


def solution():
    allLangList = set() # list of all languages
    mutualLangList = set()    # list of mutual languages
    first = True
    N = int(input())
    for _ in range(N):
        M = int(input())
        OnePupil = set()
        for __ in range(M):
            OnePupil.add(input())
        if first:
            mutualLangList = OnePupil
            first = False
        else:
            mutualLangList = mutualLangList.intersection(OnePupil)
        allLangList = allLangList.union(OnePupil)

    print(len(mutualLangList))
    for L in mutualLangList:
        print(L)
    print(len(allLangList))
    for L in allLangList:
        print(L)


def main():
    solution()

if __name__ == '__main__':
    main()
